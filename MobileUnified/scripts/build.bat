@echo off
set ROOT=%~dp0..
echo BizXtreme MobileUnified build
where java >nul 2>nul && echo Android/JVM toolchain: available || echo Android/JVM toolchain: not installed
where swift >nul 2>nul && echo Swift toolchain: available || echo Swift toolchain: not installed
where flutter >nul 2>nul && echo Flutter: available || echo Flutter: not installed
where node >nul 2>nul && echo Node/React Native: available || echo Node/React Native: not installed
if exist "%ROOT%contract\mobile_game_contract.json" echo Shared contract: OK
echo Platform SDK builds run when their respective SDKs are installed.
