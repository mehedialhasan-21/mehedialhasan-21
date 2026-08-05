"""
Markdown Processing Utility
---------------------------
Renders markdown templates using Jinja2 engine.
"""

import os
from typing import Any, Dict
from jinja2 import Environment, FileSystemLoader
from utils.logger import setup_logger

logger = setup_logger("Markdown")


class MarkdownRenderer:
    """Renders dynamic data into final Markdown format."""

    def __init__(self, template_dir: str = "assets/templates") -> None:
        self.template_dir = template_dir
        self.env = Environment(loader=FileSystemLoader(template_dir), autoescape=False)

    def render(self, template_name: str, context: Dict[str, Any]) -> str:
        """Loads template and injects dictionary context."""
        try:
            template = self.env.get_template(template_name)
            return template.render(**context)
        except Exception as err:
            logger.error(f"Failed to render template {template_name}: {err}")
            raise err
