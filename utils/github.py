"""
Advanced GitHub GraphQL v4 Client
---------------------------------
Retrieves accurate total lifetime commits, PRs, issues, and repository stats.
"""

import os
import requests
from typing import Dict, Any, List
from utils.logger import setup_logger

logger = setup_logger("GraphQLAPI")


class AdvancedGitHubClient:
    """Client utilizing GitHub GraphQL API for deep metrics."""

    GRAPHQL_URL = "https://api.github.com/graphql"

    def __init__(self, username: str, token: str = None) -> None:
        self.username = username
        self.token = token or os.getenv("GH_PAT") or os.getenv("GITHUB_TOKEN")
        self.headers = {
            "Authorization": f"bearer {self.token}",
            "User-Agent": "Advanced-Profile-Engine",
        }

    def fetch_user_metrics(self) -> Dict[str, Any]:
        """Queries GitHub GraphQL for complete user metrics."""
        query = """
        query($username: String!) {
          user(login: $username) {
            followers { totalCount }
            following { totalCount }
            repositories(first: 100, ownerAffiliations: OWNER, isFork: false, orderBy: {field: STARGAZERS, direction: DESC}) {
              totalCount
              nodes {
                name
                stargazerCount
                forkCount
                primaryLanguage { name color }
                url
                description
              }
            }
            contributionsCollection {
              totalCommitContributions
              totalPullRequestContributions
              totalIssueContributions
              totalRepositoryContributions
            }
          }
        }
        """
        try:
            response = requests.post(
                self.GRAPHQL_URL,
                json={"query": query, "variables": {"username": self.username}},
                headers=self.headers,
                timeout=10,
            )
            if response.status_code == 200:
                data = response.json().get("data", {}).get("user", {})
                return self._parse_metrics(data)
            else:
                logger.error(f"GraphQL Query Failed [{response.status_code}]: {response.text}")
        except Exception as err:
            logger.error(f"Failed fetching GraphQL metrics: {err}")

        return self._fallback_metrics()

    def _parse_metrics(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Parses GraphQL raw payload into structured data."""
        repos = data.get("repositories", {}).get("nodes", [])
        total_stars = sum(r.get("stargazerCount", 0) for r in repos)
        total_forks = sum(r.get("forkCount", 0) for r in repos)

        contribs = data.get("contributionsCollection", {})

        return {
            "followers": data.get("followers", {}).get("totalCount", 0),
            "following": data.get("following", {}).get("totalCount", 0),
            "public_repos": data.get("repositories", {}).get("totalCount", 0),
            "total_stars": total_stars,
            "total_forks": total_forks,
            "total_commits": contribs.get("totalCommitContributions", 0),
            "total_prs": contribs.get("totalPullRequestContributions", 0),
            "total_issues": contribs.get("totalIssueContributions", 0),
            "pinned_repos": repos[:4],
            "latest_repos": repos[:5],
        }

    def _fallback_metrics(self) -> Dict[str, Any]:
        """Provides default values when API fails."""
        return {
            "followers": 0,
            "following": 0,
            "public_repos": 0,
            "total_stars": 0,
            "total_forks": 0,
            "total_commits": 0,
            "total_prs": 0,
            "total_issues": 0,
            "pinned_repos": [],
            "latest_repos": [],
        }
