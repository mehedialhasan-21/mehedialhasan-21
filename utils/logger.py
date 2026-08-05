"""
Logging Utility
---------------
Provides standard application-wide logging configuration with customizable formatting.
"""

import logging
import sys


def setup_logger(name: str = "AutoProfile", level: int = logging.INFO) -> logging.Logger:
    """Configures and returns a structured logger instance."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    if not logger.handlers:
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(level)

        formatter = logging.Formatter(
            fmt="[%(asctime)s] [%(levelname)s] [%(name)s]: %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger
