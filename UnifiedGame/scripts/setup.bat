@echo off
setlocal
echo BizXtreme Unified Game dependency/toolchain check
for %%C in (python node npm java mvn dotnet cargo go cmake dart swift) do where %%C >nul 2>nul && echo [OK] %%C || echo [--] %%C not installed (optional unless selected)
where python >nul 2>nul && python -m pip install --upgrade pip --disable-pip-version-check
if exist "%~dp0..\nodejs\package.json" where npm >nul 2>nul && (cd /d "%~dp0..\nodejs" && npm install)
echo Setup/check complete. No privileged OS packages were installed.
