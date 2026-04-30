#!/usr/bin/env bash
set -euo pipefail

if ! command -v lark-cli >/dev/null 2>&1; then
  if ! command -v npm >/dev/null 2>&1; then
    echo "lark-cli is missing and npm is not available; cannot bootstrap Feishu CLI" >&2
    exit 127
  fi
  npm install -g @larksuite/cli >/dev/null
fi

FEISHU_SECRET="${FEISHU_APP_SECRET:-${FEISHUAPPSECRET:-}}"
if [ -z "$FEISHU_SECRET" ]; then
  echo "FEISHU_APP_SECRET is required in the cloud environment (FEISHUAPPSECRET alias is also accepted)" >&2
  exit 2
fi

APP_ID="${FEISHU_APP_ID:-}"
if [ -z "$APP_ID" ]; then
  echo "FEISHU_APP_ID is required in the cloud environment" >&2
  exit 2
fi

BRAND="${FEISHU_BRAND:-feishu}"

printf '%s' "$FEISHU_SECRET" \
  | lark-cli config init --app-id "$APP_ID" --app-secret-stdin --brand "$BRAND" >/dev/null

lark-cli doctor || echo "WARN: lark-cli doctor reported a non-bot issue; continuing with bot checks."
