param([int]$Port=8790)
$root=Split-Path $PSScriptRoot -Parent
$env:ASSET_BROWSER_PORT=$Port
python "$root/python/app.py"
