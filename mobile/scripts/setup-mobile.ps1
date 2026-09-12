$ErrorActionPreference='Stop'
Write-Host 'BizXtreme mobile SDK bootstrap'
if (Get-Command flutter -ErrorAction SilentlyContinue) { flutter doctor; Push-Location ../flutter; flutter pub get; Pop-Location } else { Write-Warning 'Flutter not installed. Install from https://docs.flutter.dev/get-started/install/windows' }
if (Get-Command java -ErrorAction SilentlyContinue) { java -version } else { Write-Warning 'JDK required for Android builds.' }
Write-Host 'Kotlin/Android dependencies are resolved through Gradle/Android Studio.'
Write-Host 'iOS builds require macOS/Xcode.'
