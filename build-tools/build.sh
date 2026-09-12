#!/usr/bin/env sh
set -eu
ROOT=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
command -v python3 >/dev/null 2>&1 || { echo '[DEPENDENCY] Python 3 not found.'; exit 2; }
exec python3 "$ROOT/build-tools/build.py" "$@"
