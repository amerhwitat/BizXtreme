$ErrorActionPreference='Stop'
Set-Location (Join-Path $PSScriptRoot '..')
python -m pip install -r requirements-dev.txt
python -m PyInstaller --noconfirm --clean --windowed --name BizXtreme bizxtreme\__main__.py
