#!/usr/bin/env bash
set -euo pipefail
: "${SCHEME:?Set SCHEME}"
: "${EXPORT_OPTIONS:?Set EXPORT_OPTIONS}"
xcodebuild -exportArchive -archivePath "${ARCHIVE:-build/archive/$SCHEME.xcarchive}" -exportOptionsPlist "$EXPORT_OPTIONS" -exportPath build/ipa
