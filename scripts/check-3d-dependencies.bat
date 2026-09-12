@echo off
setlocal
where git >nul 2>&1 && echo OK git || echo WARN missing git
where dotnet >nul 2>&1 && echo OK dotnet || echo WARN missing dotnet
if defined UNITY_EDITOR_PATH (echo Unity editor: %UNITY_EDITOR_PATH%) else echo Unity: set UNITY_EDITOR_PATH before automated builds
if defined UNREAL_ENGINE_ROOT (echo UE5 root: %UNREAL_ENGINE_ROOT%) else echo UE5 native plugin is maintained in BizX
endlocal
