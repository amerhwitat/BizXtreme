# Mobile, launcher, saves and P2P

BizXtreme now has Kotlin Multiplatform and Flutter mobile boundaries. Flutter's official Casual Games Toolkit provides open-source multiplatform 2D templates; Flame is an open-source Flutter game engine for mobile, desktop and web. Kotlin Multiplatform supports shared Android/iOS logic and Compose Multiplatform UI.

The mobile starting menu selects 2D/3D/4D games, wallet setup, backups, snapshots, saves, hall of fame and peer presence. Recovery phrases/private keys are never placed in game saves, logs or peer channels; wallet backup is delegated to secure platform storage or user-controlled providers.

Peer presence is consent-based. Do not persist raw IP addresses in player profiles or expose them to other users. Exact location is not inferred from IP; an optional coarse region may be self-selected. Live connection status can be displayed during the current application run.

SDK bootstrap scripts: `mobile/scripts/setup-mobile.ps1` and `.sh`.

References:
- Flutter Games: https://flutter.dev/games
- Flutter Games Toolkit: https://docs.flutter.dev/resources/games-toolkit
- Flame: https://github.com/flame-engine/flame
- Kotlin Multiplatform: https://kotlinlang.org/docs/multiplatform.html
- Android KMP guidance: https://developer.android.com/kotlin/multiplatform
