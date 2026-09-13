#!/usr/bin/env bash
set -euo pipefail
MODE=default
CASH=10000
while [[ $# -gt 0 ]]; do case "$1" in --mode) MODE="$2"; shift 2;; --cash) CASH="$2"; shift 2;; *) echo "Unknown option: $1" >&2; exit 2;; esac; done
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
PY="$(command -v python3 || command -v python)"
"$PY" "$ROOT/launcher/python/main.py" --mode "$MODE" --cash "$CASH"
