name: Auto Update GitHub Profile README

on:
  schedule:
    # Runs automatically every day at midnight UTC
    - cron: '0 0 * * *'
  workflow_dispatch:

permissions:
  contents: write

jobs:
  build-and-update:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout Repository
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Set up Python 3.12
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'
          cache: 'pip'

      - name: Install Dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Regenerate README Content
        env:
          GH_PAT: ${{ secrets.GH_PAT }}
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: |
          python update.py

      - name: Commit and Push Changes Safely
        run: |
          git config --local user.email "programmer.mehedialhasansawon21@gmail.com"
          git config --local user.name "mehedialhasan-21"

          # Stage changes safely without throwing error 128 if cache doesn't exist
          git add README.md
          git add data_cache.json || true

          # Commit only if changes actually exist
          if git diff --staged --quiet; then
            echo "No changes detected in generated content. Skipping commit."
          else
            git commit -m "chore(auto-update): regenerate profile README [skip ci]"
            git push
          fi
