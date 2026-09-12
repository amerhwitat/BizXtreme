#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
ASSET_ROOT="$ROOT/assets/art/cc0-public-domain-deck"
TMP="${TMPDIR:-/tmp}/bizxtreme-opendecks-card-art"
rm -rf "$TMP"
mkdir -p "$ASSET_ROOT"
git clone --depth 1 https://github.com/AustinGabriel/OpenDecks-Public-Domain-and-CC0-Playing-Cards "$TMP"
cp "$TMP/LICENSE" "$ASSET_ROOT/LICENSE.txt"
cp "$TMP/README.md" "$ASSET_ROOT/SOURCE_README.md"
cp -R "$TMP/svg cards" "$ASSET_ROOT/"
cp -R "$TMP/png cards" "$ASSET_ROOT/"
rm -rf "$TMP"
echo "BizXtreme CC0 card artwork installed."
