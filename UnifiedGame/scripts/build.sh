#!/usr/bin/env bash
set -u
ROOT="$(cd "$(dirname "$0")/.." && pwd)"; FAILED=0
run(){ local n="$1"; shift; echo "== $n =="; if "$@"; then :; else FAILED=$((FAILED+1)); fi; }
command -v python3 >/dev/null 2>&1 && run 'Python syntax' python3 -m py_compile "$ROOT/launcher/python/main.py" || echo '[SKIP] Python'
command -v node >/dev/null 2>&1 && run 'Node syntax' node --check "$ROOT/launcher/node/index.js" || echo '[SKIP] Node'
command -v mvn >/dev/null 2>&1 && run 'Java build' mvn -q package -DskipTests -f "$ROOT/launcher/java/pom.xml" || echo '[SKIP] Maven'
command -v cargo >/dev/null 2>&1 && run 'Rust build' cargo build --release --manifest-path "$ROOT/launcher/rust/Cargo.toml" || echo '[SKIP] Cargo'
command -v go >/dev/null 2>&1 && (cd "$ROOT/launcher/go" && run 'Go build' go build .) || echo '[SKIP] Go'
command -v dotnet >/dev/null 2>&1 && run '.NET build' dotnet build -c Release "$ROOT/launcher/csharp/BizXtreme.UnifiedGame.csproj" || echo '[SKIP] .NET'
command -v cmake >/dev/null 2>&1 && run 'CMake build' bash -c "cmake -S '$ROOT/launcher/cpp' -B '$ROOT/launcher/cpp/build' -DCMAKE_BUILD_TYPE=Release && cmake --build '$ROOT/launcher/cpp/build'" || echo '[SKIP] CMake'
(( FAILED == 0 )) || exit 1
echo 'Unified build completed for available toolchains.'
