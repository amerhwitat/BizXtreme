$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent $PSScriptRoot
$assetRoot = Join-Path $root 'assets/art/cc0-public-domain-deck'
$tmp = Join-Path $env:TEMP 'bizxtreme-opendecks-card-art'
if (Test-Path $tmp) { Remove-Item $tmp -Recurse -Force }
New-Item -ItemType Directory -Path $assetRoot -Force | Out-Null
& git clone --depth 1 https://github.com/AustinGabriel/OpenDecks-Public-Domain-and-CC0-Playing-Cards $tmp
if ($LASTEXITCODE -ne 0) { throw 'git clone failed' }
Copy-Item (Join-Path $tmp 'LICENSE') (Join-Path $assetRoot 'LICENSE.txt') -Force
Copy-Item (Join-Path $tmp 'README.md') (Join-Path $assetRoot 'SOURCE_README.md') -Force
Copy-Item (Join-Path $tmp 'svg cards') (Join-Path $assetRoot 'svg cards') -Recurse -Force
Copy-Item (Join-Path $tmp 'png cards') (Join-Path $assetRoot 'png cards') -Recurse -Force
Remove-Item $tmp -Recurse -Force
Write-Host 'BizXtreme CC0 card artwork installed.'
