@echo off
setlocal
set ASSET_BROWSER_PORT=%~1
if "%ASSET_BROWSER_PORT%"=="" set ASSET_BROWSER_PORT=8790
cd /d "%~dp0.."
python python\app.py
