@echo off
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%~dp0scripts\clean.ps1"
exit /b %ERRORLEVEL%
