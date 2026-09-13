$ErrorActionPreference='Continue'
$root=Split-Path $PSScriptRoot -Parent
Write-Host 'BizXtreme Unified Game dependency/toolchain check'
$commands=@('python','node','npm','java','mvn','dotnet','cargo','go','cmake','dart','swift')
foreach($c in $commands){$x=Get-Command $c -ErrorAction SilentlyContinue;if($x){Write-Host "[OK] $c -> $($x.Source)"}else{Write-Host "[--] $c not installed (optional unless its adapter is selected)"}}
if(Get-Command python -ErrorAction SilentlyContinue){ python -m pip install --upgrade pip --disable-pip-version-check }
if(Test-Path (Join-Path $root 'nodejs/package.json')){ if(Get-Command npm -ErrorAction SilentlyContinue){ Push-Location (Join-Path $root 'nodejs'); npm install; Pop-Location } }
Write-Host 'Setup/check complete. No privileged OS packages were installed.'
