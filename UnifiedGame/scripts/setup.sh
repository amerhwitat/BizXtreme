#!/usr/bin/env bash
set -u
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo 'BizXtreme Unified Game dependency/toolchain check'
for c in python3 node npm java mvn dotnet cargo go cmake dart swift; do if command -v "$c" >/dev/null 2>&1; then echo "[OK] $c -> $(command -v "$c")"; else echo "[--] $c not installed (optional unless selected)"; fi; done
if command -v python3 >/dev/null 2>&1; then python3 -m pip install --upgrade pip --disable-pip-version-check || true; fi
if [[ -f "$ROOT/nodejs/package.json" ]] && command -v npm >/dev/null 2>&1; then (cd "$ROOT/nodejs" && npm install); fi
echo 'Setup/check complete. No privileged OS packages were installed.'
