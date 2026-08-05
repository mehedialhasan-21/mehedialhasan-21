"""
Quote Generator Utility
-----------------------
Fetches random quotes from local fallback asset files or remote APIs.
"""

import json
import random
import os
import requests
from typing import Dict
from utils.logger import setup_logger

logger = setup_logger("Quote")


class QuoteGenerator:
    """Manages acquisition of programming quotes."""

    def __init__(self, fallback_path: str = "assets/quotes.json") -> None:
        self.fallback_path = fallback_path

    def get_random_quote(self) -> Dict[str, str]:
        """Attempts to fetch from API, falls back to local JSON on failure."""
        try:
            response = requests.get("https://api.quotable.io/random?tags=technology|famous-quotes", timeout=5)
            if response.status_code == 200:
                data = response.json()
                return {"quote": data.get("content"), "author": data.get("author")}
        except Exception as err:
            logger.debug(f"Remote quote API unavailable ({err}). Using fallback.")

        return self._get_local_fallback()

    def _get_local_fallback(self) -> Dict[str, str]:
        """Reads random quote from local assets file."""
        if os.path.exists(self.fallback_path):
            try:
                with open(self.fallback_path, "r", encoding="utf-8") as file:
                    quotes = json.load(file)
                    if quotes:
                        return random.choice(quotes)
            except Exception as err:
                logger.error(f"Error reading local quotes file: {err}")

        return {
            "quote": "First, solve the problem. Then, write the code.",
            "author": "John Johnson",
        }
