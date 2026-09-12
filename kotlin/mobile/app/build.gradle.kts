plugins { id("com.android.application"); id("org.jetbrains.kotlin.android") }
android { namespace = "com.amerhwitat.bizxtreme.mobile"; compileSdk = 36; defaultConfig { applicationId = "com.amerhwitat.bizxtreme.mobile"; minSdk = 26; targetSdk = 36; versionCode = 2; versionName = "0.2.0" }; buildTypes { release { isMinifyEnabled = false } } }
kotlin { jvmToolchain(17) }
dependencies { implementation("androidx.core:core-ktx:1.17.0"); implementation("io.github.webrtc-sdk:android:150.7871.01") }
