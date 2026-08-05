"""
Caching Mechanism Utility
-------------------------
Implements file-based caching with TTL to optimize API rate limits.
"""

import json
import os
import time
from typing import Any, Optional
from utils.logger import setup_logger

logger = setup_logger("Cache")


class CacheManager:
    """Manages simple file-based JSON caching with expiry."""

    def __init__(self, cache_file: str = "data_cache.json", default_ttl: int = 3600) -> None:
        self.cache_file = cache_file
        self.default_ttl = default_ttl
        self.cache_data: dict[str, Any] = self._load_cache()

    def _load_cache(self) -> dict[str, Any]:
        """Loads cached data from disk if exists."""
        if os.path.exists(self.cache_file):
            try:
                with open(self.cache_file, "r", encoding="utf-8") as file:
                    return json.load(file)
            except Exception as err:
                logger.warning(f"Failed to read cache file, resetting cache: {err}")
                return {}
        return {}

    def save_cache(self) -> None:
        """Persists memory cache back to file."""
        try:
            with open(self.cache_file, "w", encoding="utf-8") as file:
                json.dump(self.cache_data, file, indent=2)
        except Exception as err:
            logger.error(f"Failed to write cache file: {err}")

    def get(self, key: str) -> Optional[Any]:
        """Retrieves non-expired key from cache."""
        entry = self.cache_data.get(key)
        if entry:
            timestamp = entry.get("timestamp", 0)
            ttl = entry.get("ttl", self.default_ttl)
            if time.time() - timestamp < ttl:
                logger.debug(f"Cache HIT for key: {key}")
                return entry.get("value")
            else:
                logger.debug(f"Cache EXPIRED for key: {key}")
        return None

    def set(self, key: str, value: Any, ttl: Optional[int] = None) -> None:
        """Stores key-value pair with TTL."""
        self.cache_data[key] = {
            "timestamp": time.time(),
            "ttl": ttl if ttl is not None else self.default_ttl,
            "value": value,
        }
        self.save_cache()
