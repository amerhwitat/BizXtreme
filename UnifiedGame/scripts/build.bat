@echo off
setlocal
set ROOT=%~dp0..
set FAILED=0
where python >nul 2>nul && python -m py_compile "%ROOT%launcher\python\main.py" || set FAILED=1
where node >nul 2>nul && node --check "%ROOT%launcher\node\index.js" || set FAILED=1
where mvn >nul 2>nul && (cd /d "%ROOT%launcher\java" && mvn -q package -DskipTests) || echo [SKIP] Maven
where cargo >nul 2>nul && (cd /d "%ROOT%launcher\rust" && cargo build --release) || echo [SKIP] Cargo
where go >nul 2>nul && (cd /d "%ROOT%launcher\go" && go build .) || echo [SKIP] Go
where dotnet >nul 2>nul && dotnet build -c Release "%ROOT%launcher\csharp\BizXtreme.UnifiedGame.csproj" || echo [SKIP] .NET
where cmake >nul 2>nul && (cmake -S "%ROOT%launcher\cpp" -B "%ROOT%launcher\cpp\build" -DCMAKE_BUILD_TYPE=Release && cmake --build "%ROOT%launcher\cpp\build") || echo [SKIP] CMake
if %FAILED% neq 0 exit /b %FAILED%
echo Unified build completed for available toolchains.
