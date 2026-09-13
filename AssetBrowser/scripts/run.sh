#!/usr/bin/env sh
set -eu
ROOT="$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)"
export ASSET_BROWSER_PORT="${ASSET_BROWSER_PORT:-8790}"
exec python3 "$ROOT/python/app.py"
