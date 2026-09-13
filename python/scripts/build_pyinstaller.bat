@echo off
setlocal
cd /d "%~dp0.."
python -m pip install -r requirements-dev.txt
python -m PyInstaller --noconfirm --clean --windowed --name BizXtreme bizxtreme\__main__.py
