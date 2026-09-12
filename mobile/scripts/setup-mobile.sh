#!/usr/bin/env bash
set -euo pipefail
command -v flutter >/dev/null && (cd ../flutter && flutter pub get && flutter doctor) || echo 'Flutter is not installed; install from https://docs.flutter.dev/get-started/install/linux'
command -v java >/dev/null && java -version || echo 'JDK is required for Android builds'
echo 'Kotlin/Android dependencies are resolved through Gradle/Android Studio.'
echo 'iOS builds require macOS/Xcode.'
