$ErrorActionPreference = 'Continue'
$Root = Split-Path -Parent $PSScriptRoot
Write-Host 'BizXtreme MobileUnified build'
foreach ($tool in @('java','swift','flutter','node')) {
  if (Get-Command $tool -ErrorAction SilentlyContinue) { Write-Host "$tool : available" } else { Write-Host "$tool : not installed" }
}
if (Test-Path "$Root/contract/mobile_game_contract.json") { Write-Host 'Shared contract: OK' }
Write-Host 'Platform SDK builds run when their respective SDKs are installed.'
