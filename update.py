"""
Advanced Profile Generator Entrypoint
------------------------------------
Coordinates Async/Sync API fetching, SVG generation, and markdown compilation.
"""

import json
import os
import sys
from datetime import datetime, timezone

from utils.cache import CacheManager
from utils.github import AdvancedGitHubClient
from utils.logger import setup_logger
from utils.markdown import MarkdownRenderer
from utils.quote import QuoteGenerator
from utils.svg_generator import SVGGraphicEngine

logger = setup_logger("AdvancedMain")


class AdvancedProfileUpdater:
    """Orchestrates high-performance README updating."""

    def __init__(self, config_path: str = "config.json") -> None:
        self.config = self._load_config(config_path)
        self.cache = CacheManager(default_ttl=self.config.get("cache_ttl_seconds", 3600))
        self.github_client = AdvancedGitHubClient(username=self.config["username"])
        self.quote_gen = QuoteGenerator()
        self.renderer = MarkdownRenderer()

    def _load_config(self, path: str) -> dict:
        if not os.path.exists(path):
            logger.critical(f"Config missing at {path}")
            sys.exit(1)
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    def run(self) -> None:
        logger.info("Initializing Advanced Profile Engine...")

        # 1. Fetch GraphQL metrics
        metrics = self.github_client.fetch_user_metrics()

        # 2. Generate native SVG card
        logger.info("Rendering dynamic SVG graphics...")
        SVGGraphicEngine.generate_stats_card(metrics, "assets/stats.svg")

        # 3. Get developer quote
        quote = self.quote_gen.get_random_quote()

        # 4. Prepare compilation context
        now_utc = datetime.now(timezone.utc)
        context = {
            "config": self.config,
            "stats": metrics,
            "pinned_repos": metrics.get("pinned_repos", []),
            "quote": quote,
            "timestamps": {
                "utc_time": now_utc.strftime("%Y-%m-%d %H:%M:%S UTC"),
                "current_date": now_utc.strftime("%B %d, %Y"),
            },
        }

        # 5. Render markdown
        logger.info("Compiling template...")
        rendered = self.renderer.render("README.template.md", context)

        # 6. Save if changed
        readme_path = "README.md"
        if os.path.exists(readme_path):
            with open(readme_path, "r", encoding="utf-8") as f:
                if f.read() == rendered:
                    logger.info("No modifications needed. Profile is up to date.")
                    return

        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(rendered)

        logger.info("Advanced Profile README generated successfully!")


if __name__ == "__main__":
    updater = AdvancedProfileUpdater()
    updater.run()
