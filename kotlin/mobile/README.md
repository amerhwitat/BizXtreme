# BizXtreme Kotlin Mobile

Android mobile implementation in Kotlin 2.4.20, isolated under `kotlin/mobile/`. It exposes a native entry point for the BizXtreme application while preserving the existing desktop, web, game, wallet, and language-specific implementations.

The mobile boundary is prepared for the portfolio 128D state contract and authenticated opt-in P2P fabric. Cleartext traffic is disabled by default. The structure can be extended to Kotlin Multiplatform/iOS without coupling the existing implementations.

Build with Android Studio using JDK 17, AGP 9.4.0, compile/target SDK 36.
