$ErrorActionPreference = 'Stop'
Write-Host 'BizXtreme 3D dependency check'
foreach ($tool in @('git','dotnet')) {
  if (Get-Command $tool -ErrorAction SilentlyContinue) { Write-Host "OK  $tool" } else { Write-Warning "Missing required/optional tool: $tool" }
}
if ($env:UNITY_EDITOR_PATH) { Write-Host "UNITY_EDITOR_PATH=$env:UNITY_EDITOR_PATH" } else { Write-Host 'Unity: set UNITY_EDITOR_PATH for automated project builds.' }
if ($env:UNREAL_ENGINE_ROOT) { Write-Host "UNREAL_ENGINE_ROOT=$env:UNREAL_ENGINE_ROOT" } else { Write-Host 'UE5: use BizX/Unreal5/BizXUnreal for the shared native plugin.' }
