# BizXtreme

BizXtreme is the extended BizX application/game repository, including WebGL/Three.js, Unity/C#, wallet, crypto, game, Aurora, Chimera integration, Kotlin mobile and Flutter mobile material.

## Source-code citation index

| Area | Source |
|---|---|
| Windows Visual C++ | [desktop/vcpp/](desktop/vcpp/) |
| Windows C# / WPF | [desktop/dotnet/](desktop/dotnet/) |
| Unity 3D C# package | [Unity3D/](Unity3D/) |
| Portable 3D assets | [3D/assets/](3D/assets/) |
| Realtime rendering | [rendering/](rendering/) |
| Multi-chain crypto | [crypto/](crypto/) |
| Game/store/storyboards | [game-store/](game-store/) |
| Kotlin mobile | [mobile/kotlin/](mobile/kotlin/) |
| Flutter mobile | [mobile/flutter/](mobile/flutter/) |
| P2P/presence policy | [network/](network/) |
| Node.js | [nodejs/](nodejs/) |
| Java | [java/](java/) |
| Python | [python/](python/) |
| JavaScript | [javascript/](javascript/) |
| TypeScript | [typescript/](typescript/) |
| Web | [web/](web/) |
| Three.js/WebGL | [threejs/](threejs/) |
| Existing Unity/C# | [Assets/](Assets/) |
| Apple/Swift | [apple/](apple/) |
| Documentation | [docs/](docs/) |

## Mobile game hub

Kotlin Multiplatform and Flutter shells now provide a common starting menu for 2D storyboard games, 3D worlds, 4D time-indexed worlds, wallet setup, secure backup/snapshot hooks, saves, hall of fame, store content and opt-in peer presence.

Flutter's official Games Toolkit provides open-source multiplatform 2D templates and Flame provides a modular Flutter game engine for mobile, desktop and web. Kotlin Multiplatform supports shared Android/iOS logic and Compose Multiplatform UI.

## Wallets, saves and snapshots

Wallet secrets are isolated from gameplay. Recovery phrases/private keys must stay in platform secure storage or a user-controlled wallet provider and never be copied into saves, logs, screenshots, telemetry or peer traffic. Backup manifests describe state without containing secret material.

## P2P/presence

Presence is consent-based. The client uses a random peer ID and can display live connected/disconnected state. Raw IP addresses are not exposed to other users or stored in player profiles. Exact location is not inferred from IP; an optional coarse region can be self-selected.

## Storyboards and store

`game-store/storyboards/` contains license-gated templates for 2D/3D/4D implementations. Public accessibility is not treated as a reuse license. Imports preserve source, license, attribution and integrity metadata.

## External documentation citations

- Flutter Games: https://flutter.dev/games
- Flutter Games Toolkit: https://docs.flutter.dev/resources/games-toolkit
- Flame: https://github.com/flame-engine/flame
- Kotlin Multiplatform: https://kotlinlang.org/docs/multiplatform.html
- Android Kotlin Multiplatform: https://developer.android.com/kotlin/multiplatform
- Tether WDK: https://wdk.tether.io/
- WalletConnect Specifications: https://github.com/WalletConnect/walletconnect-specs
- Wallet Standard: https://github.com/wallet-standard/wallet-standard
- Uniswap Smart Order Router: https://github.com/Uniswap/smart-order-router
- OpenGameArt: https://opengameart.org/
- Poly Haven license: https://polyhaven.com/license
- Poly Haven API: https://api.polyhaven.com/
