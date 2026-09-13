@echo off
setlocal
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%~dp0scripts\install-deps.ps1" %*
exit /b %ERRORLEVEL%
