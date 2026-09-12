@echo off
setlocal
set ROOT=%~dp0..
where python >nul 2>&1 || (echo [DEPENDENCY] Python 3 not found.&exit /b 2)
python "%ROOT%build-tools\build.py" %*
exit /b %ERRORLEVEL%
