param([ValidateSet('default','tycoon','sandbox','multiplayer')][string]$Mode='default',[double]$Cash=10000)
$ErrorActionPreference='Stop'
$root=Split-Path $PSScriptRoot -Parent
$py=Get-Command python -ErrorAction SilentlyContinue
if(-not $py){ $py=Get-Command python3 -ErrorAction SilentlyContinue }
if(-not $py){ throw 'Python 3.10+ is required for the canonical unified runtime.' }
& $py.Source (Join-Path $root 'launcher/python/main.py') --mode $Mode --cash $Cash
exit $LASTEXITCODE
