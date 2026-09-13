#!/usr/bin/env bash
set -uo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"; MODE="${1:-all}"; LOG_DIR="$ROOT/build/logs"; mkdir -p "$LOG_DIR"; LOG="$LOG_DIR/build.log"; : > "$LOG"; FAILURES=0
if [[ "$MODE" != "no-install" ]]; then "$ROOT/scripts/install-deps.sh" || FAILURES=$((FAILURES+1)); fi
while IFS= read -r -d '' f; do d="$(dirname "$f")"; case "$(basename "$f")" in
package.json) echo "== Node/TypeScript: $d =="; (cd "$d"; [[ -f package-lock.json || -f npm-shrinkwrap.json ]] && npm ci || npm install; npm run build --if-present; npm test --if-present) || FAILURES=$((FAILURES+1));;
pyproject.toml|requirements.txt) echo "== Python: $d =="; (cd "$d"; [[ -f pyproject.toml ]] && python3 -m pip install -e .; [[ -f requirements.txt ]] && python3 -m pip install -r requirements.txt; python3 -m pytest) || FAILURES=$((FAILURES+1));;
Cargo.toml) echo "== Rust: $d =="; (cd "$d"; cargo fetch; cargo build --workspace; cargo test --workspace) || FAILURES=$((FAILURES+1));;
go.mod) echo "== Go: $d =="; (cd "$d"; go mod download; go build ./...; go test ./...) || FAILURES=$((FAILURES+1));;
pom.xml) echo "== Java/Maven: $d =="; (cd "$d"; [[ -x mvnw ]] && ./mvnw -B test package || mvn -B test package) || FAILURES=$((FAILURES+1));;
build.gradle|build.gradle.kts) echo "== JVM/Gradle: $d =="; (cd "$d"; [[ -x gradlew ]] && ./gradlew build || gradle build) || FAILURES=$((FAILURES+1));;
CMakeLists.txt) echo "== C/C++: $d =="; (cd "$d"; cmake -S . -B build; cmake --build build --parallel) || FAILURES=$((FAILURES+1));;
Package.swift) echo "== Swift: $d =="; (cd "$d"; swift build; swift test) || FAILURES=$((FAILURES+1));;
pubspec.yaml) echo "== Dart: $d =="; (cd "$d"; dart pub get; dart test) || FAILURES=$((FAILURES+1));;
composer.json) echo "== PHP: $d =="; (cd "$d"; composer install --no-interaction --prefer-dist; [[ ! -f phpunit.xml ]] || vendor/bin/phpunit) || FAILURES=$((FAILURES+1));;
Gemfile) echo "== Ruby: $d =="; (cd "$d"; bundle install; bundle exec rake) || FAILURES=$((FAILURES+1));;
esac; done < <(find "$ROOT" -type f \( -name package.json -o -name pyproject.toml -o -name requirements.txt -o -name Cargo.toml -o -name go.mod -o -name pom.xml -o -name build.gradle -o -name build.gradle.kts -o -name CMakeLists.txt -o -name Package.swift -o -name pubspec.yaml -o -name composer.json -o -name Gemfile \) -not -path '*/node_modules/*' -not -path '*/target/*' -not -path '*/build/*' -not -path '*/.git/*' -print0 | sort -z -u)
echo "Build complete; failures=$FAILURES; log=$LOG" | tee "$LOG"; exit "$FAILURES"
