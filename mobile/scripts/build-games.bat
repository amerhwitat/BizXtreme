@echo off
setlocal
cd /d "%~dp0..\flutter"
where flutter >nul 2>nul
if errorlevel 1 (echo Flutter SDK not found. Install Flutter and retry.&exit /b 1)
flutter pub get
if errorlevel 1 exit /b %errorlevel%
flutter analyze
if errorlevel 1 exit /b %errorlevel%
flutter test
if errorlevel 1 exit /b %errorlevel%
echo BizXtreme mobile game checks completed.
