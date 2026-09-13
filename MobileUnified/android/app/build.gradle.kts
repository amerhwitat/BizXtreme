plugins {
    id("com.android.application")
    id("org.jetbrains.kotlin.android")
    id("org.jetbrains.kotlin.plugin.compose")
}

android { namespace = "io.amerhwitat.bizxtreme.mobile"; compileSdk = 35
    defaultConfig { applicationId = "io.amerhwitat.bizxtreme.mobile"; minSdk = 26; targetSdk = 35; versionCode = 1; versionName = "1.0" }
}

dependencies {
    implementation(platform("androidx.compose:compose-bom:2025.08.00"))
    implementation("androidx.activity:activity-compose:1.10.1")
    implementation("androidx.compose.material3:material3")
}
