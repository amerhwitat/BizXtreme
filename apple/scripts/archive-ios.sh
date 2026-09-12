#!/usr/bin/env bash
set -euo pipefail
: "${SCHEME:?Set SCHEME}"
: "${PROJECT_OR_WORKSPACE:?Set PROJECT_OR_WORKSPACE}"
mkdir -p build/archive
if [[ "$PROJECT_OR_WORKSPACE" == *.xcworkspace ]]; then xcodebuild -workspace "$PROJECT_OR_WORKSPACE" -scheme "$SCHEME" -configuration Release -destination 'generic/platform=iOS' -archivePath "build/archive/$SCHEME.xcarchive" archive; else xcodebuild -project "$PROJECT_OR_WORKSPACE" -scheme "$SCHEME" -configuration Release -destination 'generic/platform=iOS' -archivePath "build/archive/$SCHEME.xcarchive" archive; fi
