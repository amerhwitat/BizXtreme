@echo off
setlocal
set ROOT=%~dp0..
set ASSET_ROOT=%ROOT%\assets\art\cc0-public-domain-deck
set TMP=%TEMP%\bizxtreme-opendecks-card-art
if exist "%TMP%" rmdir /s /q "%TMP%"
if not exist "%ASSET_ROOT%" mkdir "%ASSET_ROOT%"
git clone --depth 1 https://github.com/AustinGabriel/OpenDecks-Public-Domain-and-CC0-Playing-Cards "%TMP%"
if errorlevel 1 exit /b 1
xcopy "%TMP%\LICENSE" "%ASSET_ROOT%\" /Y >nul
xcopy "%TMP%\README.md" "%ASSET_ROOT%\" /Y >nul
xcopy "%TMP%\svg cards" "%ASSET_ROOT%\svg cards\" /E /I /Y >nul
xcopy "%TMP%\png cards" "%ASSET_ROOT%\png cards\" /E /I /Y >nul
rmdir /s /q "%TMP%"
echo BizXtreme CC0 card artwork installed.
