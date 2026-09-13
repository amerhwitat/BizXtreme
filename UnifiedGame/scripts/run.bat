@echo off
setlocal
set MODE=default
set CASH=10000
:parse
if "%~1"=="" goto run
if /I "%~1"=="--mode" set MODE=%~2& shift&shift&goto parse
if /I "%~1"=="--cash" set CASH=%~2& shift&shift&goto parse
echo Unknown option: %~1
exit /b 2
:run
set ROOT=%~dp0..
where python >nul 2>nul || (echo Python 3.10+ is required.& exit /b 1)
python "%ROOT%launcher\python\main.py" --mode %MODE% --cash %CASH%
exit /b %ERRORLEVEL%
