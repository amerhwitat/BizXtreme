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
| Card games & T-Rex | [docs/CARD_GAMES_AND_TREX.md](docs/CARD_GAMES_AND_TREX.md) |
| Public release landing page | [docs/index.md](docs/index.md) |
| Kotlin mobile | [mobile/kotlin/](mobile/kotlin/) |
| Flutter mobile | [mobile/flutter/](mobile/flutter/) |
| P2P/presence policy | [network/](network/) |
| Client/server/host networking | [network/ClientServerNetwork.md](network/ClientServerNetwork.md) |
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

The main menu now includes Texas Hold’em Poker, Blackjack, a Classic Card Suite (Klondike, FreeCell, Hearts, Spades, Crazy Eights and War), and an original T-Rex Runner alongside the existing 2D/3D/4D worlds, wallet, saves, Hall of Fame, store and peer-presence features.

## Artwork and game flow

Original vector splash and card-table artwork lives under `mobile/flutter/assets/art/`. Game flow metadata lives in `game-store/storyboards/card-games-and-trex.json`. Card rendering is data-driven from a standard deck model.

## Wallets, saves and snapshots

Wallet secrets are isolated from gameplay. Recovery phrases/private keys must stay in platform secure storage or a user-controlled wallet provider and never be copied into saves, logs, screenshots, telemetry or peer traffic.

## P2P/presence and client/server networking

Presence is consent-based. `network/ClientServerNetwork.md` adds Client, Server, Host and Hybrid modes alongside P2P. Networking launches from the existing application UI. Users select a nickname and avatar, and can upload a validated local PNG/JPEG/WebP avatar when built-in choices are unavailable. Host mode runs a local client against the embedded server so host actions follow the same routing and authorization path as remote clients.

## Public release

`docs/index.md` is the public project landing page source and `.github/workflows/publish-docs.yml` can publish it through GitHub Pages when Pages is enabled for the repository.

## External documentation citations

- Flutter Games: https://flutter.dev/games
- Flutter Games Toolkit: https://docs.flutter.dev/resources/games-toolkit
- Flame: https://github.com/flame-engine/flame
- Kotlin Multiplatform: https://kotlinlang.org/docs/multiplatform.html
- Texas Hold’em rules: https://bicyclecards.com/how-to-play/texas-holdem-poker
- Blackjack rules: https://bicyclecards.com/how-to-play/blackjack/
- Tether WDK: https://wdk.tether.io/
- WalletConnect Specifications: https://github.com/WalletConnect/walletconnect-specs
- Wallet Standard: https://github.com/wallet-standard/wallet-standard
- OpenGameArt: https://opengameart.org/
- Poly Haven license: https://polyhaven.com/license
- Poly Haven API: https://api.polyhaven.com/
