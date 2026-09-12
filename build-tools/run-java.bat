@echo off
setlocal
set ROOT=%~dp0..
call "%ROOT%build-tools\build.bat" --only java
if errorlevel 1 exit /b %ERRORLEVEL%
for /r "%ROOT%build" %%J in (*.jar) do (
 echo [RUN] java -jar "%%J"
 java -jar "%%J"
 exit /b %ERRORLEVEL%
)
echo [RUN] No packaged Java JAR detected; compilation completed.
