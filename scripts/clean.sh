#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"; find "$ROOT" -type d \( -name node_modules -o -name target -o -name build -o -name bin -o -name obj -o -name .venv -o -name __pycache__ \) -prune -exec rm -rf {} +; echo 'Clean complete.'
