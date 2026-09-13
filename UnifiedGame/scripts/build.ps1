$ErrorActionPreference='Continue'
$root=Split-Path $PSScriptRoot -Parent
$failed=0
function Run($name,$exe,$args,$cwd){if(Get-Command $exe -ErrorAction SilentlyContinue){Write-Host "== $name ==";Push-Location $cwd;& $exe @args;if($LASTEXITCODE -ne 0){$script:failed++};Pop-Location}else{Write-Host "[SKIP] $name ($exe not installed)"}}
Run 'Python syntax' 'python' @('-m','py_compile',(Join-Path $root 'launcher/python/main.py')) $root
Run 'Node syntax' 'node' @('--check',(Join-Path $root 'launcher/node/index.js')) $root
Run 'Java build' 'mvn' @('-q','package','-DskipTests') (Join-Path $root 'launcher/java')
Run 'Rust build' 'cargo' @('build','--release') (Join-Path $root 'launcher/rust')
Run 'Go build' 'go' @('build','-o','bizxtreme-unified.exe','.') (Join-Path $root 'launcher/go')
Run '.NET build' 'dotnet' @('build','-c','Release') (Join-Path $root 'launcher/csharp')
Run 'CMake configure/build' 'cmake' @('-S',(Join-Path $root 'launcher/cpp'),'-B',(Join-Path $root 'launcher/cpp/build'),'-DCMAKE_BUILD_TYPE=Release') $root
if(Get-Command cmake -ErrorAction SilentlyContinue){& cmake --build (Join-Path $root 'launcher/cpp/build') --config Release;if($LASTEXITCODE -ne 0){$failed++}}
if($failed){exit 1}; Write-Host 'Unified build completed for available toolchains.'
