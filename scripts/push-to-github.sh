#!/bin/bash
# push-to-github.sh - Push daily report from OpenClaw workspace to GitHub repo
# Usage: bash scripts/push-to-github.sh [YYYY-MM-DD]
# If no date given, uses today (Asia/Shanghai timezone)

set -euo pipefail

REPO_DIR="/tmp/ai-film-daily"
REPO_URL="https://github.com/chenmozhe008/ai-film-daily.git"
WORKSPACE="/root/.openclaw/workspace/skills/ai-daily-digest"

DATE="${1:-$(TZ=Asia/Shanghai date +%Y-%m-%d)}"
echo "[push] Date: $DATE"

# Find the daily report in workspace
REPORT=""
for pattern in "${WORKSPACE}/ai-daily-digest-${DATE}.md" "${WORKSPACE}/digest-${DATE}.md" "${WORKSPACE}/${DATE}.md"; do
  if [ -f "$pattern" ]; then
    REPORT="$pattern"
    break
  fi
done

if [ -z "$REPORT" ]; then
  echo "[push] ERROR: No report found for $DATE in workspace"
  exit 1
fi

# Clone or pull
if [ -d "$REPO_DIR/.git" ]; then
  cd "$REPO_DIR" && git pull --rebase origin main
else
  rm -rf "$REPO_DIR"
  git clone "$REPO_URL" "$REPO_DIR"
fi

cd "$REPO_DIR"

# Copy report
cp "$REPORT" "daily/${DATE}.md"

# Sync sources (no secrets in these files)
cp "${WORKSPACE}/references/rss-feeds.json" sources/ 2>/dev/null || true
cp "${WORKSPACE}/references/x-lists.json" sources/ 2>/dev/null || true
cp "${WORKSPACE}/references/keywords.json" sources/ 2>/dev/null || true
cp "${WORKSPACE}/references/kol-sources.json" sources/ 2>/dev/null || true
cp "${WORKSPACE}/references/blacklist.txt" sources/ 2>/dev/null || true
cp "${WORKSPACE}/references/template.md" sources/ 2>/dev/null || true

# Commit and push
git add daily/ sources/
if git diff --cached --quiet; then
  echo "[push] No changes to commit"
else
  git commit -m "daily: ${DATE} report"
  git push origin main
  echo "[push] Published ${DATE} report to GitHub"
fi
