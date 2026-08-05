"""
Dynamic Native SVG Graphic Engine
----------------------------------
Generates a dark-mode summary card directly without external standard dependencies.
"""

import os


class SVGGraphicEngine:
    """Generates custom SVG widgets for GitHub Profile."""

    @staticmethod
    def generate_stats_card(metrics: dict, output_path: str = "assets/stats.svg") -> None:
        """Renders an ultra-modern dark glassmorphism stats widget SVG."""
        commits = metrics.get("total_commits", 0)
        stars = metrics.get("total_stars", 0)
        prs = metrics.get("total_prs", 0)
        issues = metrics.get("total_issues", 0)

        svg_content = f"""<svg fill="none" viewBox="0 0 480 210" width="480" height="210" xmlns="http://www.w3.org/2000/svg">
  <style>
    .bg {{ fill: #0d1117; stroke: #30363d; stroke-width: 1px; rx: 12px; }}
    .title {{ font: bold 16px 'Segoe UI', Ubuntu, sans-serif; fill: #38bdf8; }}
    .label {{ font: 13px 'Segoe UI', Ubuntu, sans-serif; fill: #94a3b8; }}
    .value {{ font: bold 14px 'Segoe UI', Ubuntu, sans-serif; fill: #f8fafc; }}
    .accent {{ fill: #818cf8; }}
  </style>
  <rect width="100%" height="100%" class="bg" />
  
  <text x="25" y="35" class="title">🚀 Lifetime Contribution Metrics</text>
  <line x1="25" y1="48" x2="455" y2="48" stroke="#21262d" stroke-width="1"/>

  <g transform="translate(25, 75)">
    <circle cx="10" cy="-4" r="5" class="accent"/>
    <text x="25" y="0" class="label">Total Commits (This Year):</text>
    <text x="430" y="0" class="value" text-anchor="end">{commits}</text>
  </g>

  <g transform="translate(25, 110)">
    <circle cx="10" cy="-4" r="5" fill="#f59e0b"/>
    <text x="25" y="0" class="label">Total Stars Earned:</text>
    <text x="430" y="0" class="value" text-anchor="end">{stars}</text>
  </g>

  <g transform="translate(25, 145)">
    <circle cx="10" cy="-4" r="5" fill="#10b981"/>
    <text x="25" y="0" class="label">Pull Requests Opened:</text>
    <text x="430" y="0" class="value" text-anchor="end">{prs}</text>
  </g>

  <g transform="translate(25, 180)">
    <circle cx="10" cy="-4" r="5" fill="#ec4899"/>
    <text x="25" y="0" class="label">Total Issues Opened:</text>
    <text x="430" y="0" class="value" text-anchor="end">{issues}</text>
  </g>
</svg>
"""
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(svg_content)
