#!/usr/bin/env sh
set -eu
ROOT=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
"$ROOT/build-tools/build.sh" --only java
JAR=$(find "$ROOT/build" -type f -name '*.jar' -print -quit 2>/dev/null || true)
if [ -n "$JAR" ]; then echo "[RUN] java -jar $JAR"; exec java -jar "$JAR"; fi
echo '[RUN] No packaged Java JAR detected; compilation completed.'
