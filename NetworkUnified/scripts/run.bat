@echo off
setlocal
set "R=%~dp0.."
if "%NETWORK_API_IMPL%"=="" set "NETWORK_API_IMPL=python"
if /I "%NETWORK_API_IMPL%"=="python" python "%R%\python\app.py" & goto :eof
if /I "%NETWORK_API_IMPL%"=="node" node "%R%\node\app.js" & goto :eof
if /I "%NETWORK_API_IMPL%"=="typescript" npx --yes tsx "%R%\typescript\app.ts" & goto :eof
if /I "%NETWORK_API_IMPL%"=="go" go run "%R%\go\main.go" & goto :eof
if /I "%NETWORK_API_IMPL%"=="rust" cargo run --manifest-path "%R%\rust\Cargo.toml" & goto :eof
if /I "%NETWORK_API_IMPL%"=="java" javac "%R%\java\Main.java" -d "%R%\java\out" && java -cp "%R%\java\out" Main & goto :eof
if /I "%NETWORK_API_IMPL%"=="csharp" dotnet run --project "%R%\csharp" & goto :eof
if /I "%NETWORK_API_IMPL%"=="cpp" c++ -std=c++17 "%R%\cpp\main.cpp" -o "%R%\cpp\network-api.exe" && "%R%\cpp\network-api.exe" & goto :eof
if /I "%NETWORK_API_IMPL%"=="dart" dart run "%R%\dart\bin\main.dart" & goto :eof
if /I "%NETWORK_API_IMPL%"=="kotlin" kotlinc "%R%\kotlin\Main.kt" -include-runtime -d "%R%\kotlin\network-api.jar" && java -jar "%R%\kotlin\network-api.jar" & goto :eof
if /I "%NETWORK_API_IMPL%"=="swift" swift "%R%\swift\main.swift" & goto :eof
if /I "%NETWORK_API_IMPL%"=="php" php "%R%\php\main.php" & goto :eof
if /I "%NETWORK_API_IMPL%"=="ruby" ruby "%R%\ruby\main.rb" & goto :eof
echo Unknown NETWORK_API_IMPL=%NETWORK_API_IMPL%
exit /b 2
