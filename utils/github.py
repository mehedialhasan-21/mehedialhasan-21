"""
GitHub REST API Client Utility
------------------------------
Handles authenticated requests, pagination, statistics gathering, and retries.
"""

import os
import time
from typing import Any, Dict, List, Optional
import requests
from utils.logger import setup_logger

logger = setup_logger("GitHubAPI")


class GitHubClient:
    """Client for interacting with GitHub REST API."""

    BASE_URL = "https://api.github.com"

    def __init__(self, username: str, token: Optional[str] = None) -> None:
        self.username = username
        self.token = token or os.getenv("GH_PAT") or os.getenv("GITHUB_TOKEN")
        self.headers = {
            "Accept": "application/vnd.github.v3+json",
            "User-Agent": "Auto-Profile-README-Generator",
        }
        if self.token:
            self.headers["Authorization"] = f"token {self.token}"
        else:
            logger.warning("No GitHub Token provided. Requests may face strict rate limits.")

    def _request(self, endpoint: str, params: Optional[Dict[str, Any]] = None, retries: int = 3) -> Optional[Any]:
        """Executes GET request with exponential backoff retry mechanism."""
        url = f"{self.BASE_URL}{endpoint}" if not endpoint.startswith("http") else endpoint
        for attempt in range(1, retries + 1):
            try:
                response = requests.get(url, headers=self.headers, params=params, timeout=10)
                if response.status_code == 200:
                    return response.json()
                elif response.status_code == 403 and "rate limit" in response.text.lower():
                    logger.warning("GitHub API rate limit hit. Waiting before retry...")
                    time.sleep(5 * attempt)
                else:
                    logger.error(f"API Request failed [{response.status_code}]: {response.text}")
            except requests.RequestException as err:
                logger.error(f"Request exception on attempt {attempt}: {err}")
                time.sleep(2 * attempt)
        return None

    def get_user_profile(self) -> Dict[str, Any]:
        """Fetches public profile data."""
        data = self._request(f"/users/{self.username}")
        return data or {}

    def get_user_repos(self) -> List[Dict[str, Any]]:
        """Fetches all public repositories for user."""
        repos = []
        page = 1
        while True:
            data = self._request(f"/users/{self.username}/repos", params={"per_page": 100, "page": page, "type": "owner"})
            if not data or not isinstance(data, list):
                break
            repos.extend(data)
            if len(data) < 100:
                break
            page += 1
        return repos

    def get_recent_activity(self, limit: int = 5) -> List[Dict[str, Any]]:
        """Fetches recent public user activities."""
        events = self._request(f"/users/{self.username}/events/public", params={"per_page": 15})
        if not events or not isinstance(events, list):
            return []

        formatted_events = []
        for event in events:
            if len(formatted_events) >= limit:
                break
            event_type = event.get("type", "")
            repo_name = event.get("repo", {}).get("name", "")
            created_at = event.get("created_at", "")[:10]

            type_map = {
                "PushEvent": "🔀 Pushed commits to",
                "CreateEvent": "✨ Created repository/branch at",
                "WatchEvent": "⭐ Starred repository",
                "PullRequestEvent": "🔀 Opened PR at",
                "IssuesEvent": "📌 Interacted with issue at",
            }

            if event_type in type_map:
                formatted_events.append({
                    "type": type_map[event_type],
                    "repo_name": repo_name,
                    "created_at": created_at,
                })

        return formatted_events

    def calculate_stats(self) -> Dict[str, Any]:
        """Calculates total stars, total forks, estimated commits, and profile metrics."""
        profile = self.get_user_profile()
        repos = self.get_user_repos()

        total_stars = sum(repo.get("stargazers_count", 0) for repo in repos)
        total_forks = sum(repo.get("forks_count", 0) for repo in repos)
        
        # Estimate total commits across user repositories
        total_commits = 0
        for repo in repos:
            if not repo.get("fork", False):
                # Approximation formula based on repository activity size
                total_commits += repo.get("size", 0) // 10 + 1

        sorted_repos = sorted(repos, key=lambda x: x.get("updated_at", ""), reverse=True)

        return {
            "followers": profile.get("followers", 0),
            "following": profile.get("following", 0),
            "public_repos": profile.get("public_repos", 0),
            "total_stars": total_stars,
            "total_forks": total_forks,
            "total_commits": max(total_commits, profile.get("public_repos", 0) * 5),
            "all_repos": repos,
            "latest_repos": sorted_repos[:5],
            "pinned_repos": sorted(repos, key=lambda x: x.get("stargazers_count", 0), reverse=True)[:4],
        }
