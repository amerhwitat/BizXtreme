#!/usr/bin/env bash
set -u
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "BizXtreme MobileUnified build"
for tool in java swift flutter node; do
  if command -v "$tool" >/dev/null 2>&1; then echo "$tool: available"; else echo "$tool: not installed"; fi
done
[ -f "$ROOT/contract/mobile_game_contract.json" ] && echo "Shared contract: OK"
echo "Platform SDK builds run when their respective SDKs are installed."
