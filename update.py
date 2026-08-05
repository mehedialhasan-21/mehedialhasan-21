"""
Auto GitHub Profile README Generator Core Entrypoint
--------------------------------------------------
Orchestrates data fetching, processing, rendering, and safe atomic writing.
"""

import json
import os
import sys
from datetime import datetime, timezone
import requests

from utils.cache import CacheManager
from utils.github import GitHubClient
from utils.logger import setup_logger
from utils.markdown import MarkdownRenderer
from utils.quote import QuoteGenerator

logger = setup_logger("Main")


class ProfileUpdater:
    """Main orchestrator for profile generation."""

    def __init__(self, config_path: str = "config.json") -> None:
        self.config = self._load_config(config_path)
        self.cache = CacheManager(default_ttl=self.config.get("cache_ttl_seconds", 3600))
        self.github_client = GitHubClient(username=self.config["username"])
        self.quote_gen = QuoteGenerator()
        self.renderer = MarkdownRenderer()

    def _load_config(self, path: str) -> dict:
        """Loads system configuration."""
        if not os.path.exists(path):
            logger.critical(f"Config file not found at {path}")
            sys.exit(1)
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    def fetch_codeforces_data(self) -> dict:
        """Optional Codeforces integration."""
        cf_config = self.config.get("integrations", {}).get("codeforces", {})
        if not cf_config.get("enabled"):
            return {}

        username = cf_config.get("username")
        cached = self.cache.get(f"codeforces_{username}")
        if cached:
            return cached

        try:
            res = requests.get(f"https://codeforces.com/api/user.info?handles={username}", timeout=5)
            if res.status_code == 200:
                result = res.json().get("result", [{}])[0]
                data = {
                    "rating": result.get("rating", "N/A"),
                    "rank": result.get("rank", "N/A").title(),
                }
                self.cache.set(f"codeforces_{username}", data)
                return data
        except Exception as e:
            logger.warning(f"Failed to fetch Codeforces data: {e}")
        return {}

    def run(self) -> None:
        """Executes full update workflow."""
        logger.info("Starting Profile README Generation Pipeline...")

        # 1. Fetch GitHub Data
        logger.info("Fetching GitHub statistics...")
        stats_data = self.github_client.calculate_stats()
        recent_activity = self.github_client.get_recent_activity()

        # 2. Fetch External Integrations
        logger.info("Fetching optional integrations...")
        codeforces_data = self.fetch_codeforces_data()

        # 3. Get Quote
        quote = self.quote_gen.get_random_quote()

        # 4. Prepare Context
        now_utc = datetime.now(timezone.utc)
        context = {
            "config": self.config,
            "stats": stats_data,
            "pinned_repos": stats_data.get("pinned_repos", []),
            "latest_repos": stats_data.get("latest_repos", []),
            "recent_activities": recent_activity,
            "quote": quote,
            "external": {
                "codeforces": codeforces_data,
            },
            "timestamps": {
                "utc_time": now_utc.strftime("%Y-%m-%d %H:%M:%S UTC"),
                "current_date": now_utc.strftime("%B %d, %Y"),
            },
        }

        # 5. Render Template
        logger.info("Rendering README.md from template...")
        rendered_content = self.renderer.render("README.template.md", context)

        # 6. Check existing file to avoid unnecessary IO / commits
        readme_path = "README.md"
        if os.path.exists(readme_path):
            with open(readme_path, "r", encoding="utf-8") as f:
                existing_content = f.read()

            if existing_content == rendered_content:
                logger.info("No content changes detected. README is up to date.")
                return

        # 7. Write updated content
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(rendered_content)

        logger.info("README.md updated successfully!")


if __name__ == "__main__":
    updater = ProfileUpdater()
    updater.run()
