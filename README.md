# BizXtreme

BizXtreme is the extended BizX application/game repository, including WebGL/Three.js, Unity/C#, wallet, crypto, game, Aurora, Chimera integration and Kotlin mobile material.

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
| Node.js | [nodejs/](nodejs/) |
| Java | [java/](java/) |
| Python | [python/](python/) |
| JavaScript | [javascript/](javascript/) |
| TypeScript | [typescript/](typescript/) |
| Web | [web/](web/) |
| Three.js/WebGL | [threejs/](threejs/) |
| Existing Unity/C# | [Assets/](Assets/) |
| Kotlin mobile | [kotlin/mobile/](kotlin/mobile/) |
| Apple/Swift | [apple/](apple/) |
| Chimera integration | [chimera/](chimera/) |
| Aurora integration | [aurora_integration.json](aurora_integration.json) |
| Documentation | [docs/](docs/) |

## Realtime rendering and open game content

`rendering/` contains the renderer capability architecture for Unity, Godot 4, OGRE, Bevy, bgfx, Filament and Three.js. `game-store/` adds a license-aware catalog for free, donation and low-price 2D/3D/4D storyboard/game content. 4D storyboards are represented as time-indexed 2D/3D states. Public visibility is never treated as a reuse license; imports retain source, license, attribution and SHA-256 metadata.

## Multi-chain crypto

`crypto/` adds a chain-agnostic, self-custody-first API for balance discovery, receive addresses, send intents, buy/sell provider intents, swaps/exchanges and sweep planning across Bitcoin/UTXO, EVM, Solana, TON and additional adapter-defined networks.

Private keys and seed phrases stay outside Unity assets, scenes, saves, telemetry and logs. Live signing is delegated to a user-controlled wallet/provider and requires explicit confirmation. Sweep is a plan until the user approves transactions.

Research and interoperability references include Tether WDK, Wallet Standard, WalletConnect specifications and Uniswap Smart Order Router. Third-party source is not copied into this repository merely because it is public.

## Licensing

New and modified BizXtreme code is intended for GNU GPL v3 or later. Third-party assets, Unity packages, wallet SDKs, exchange providers and engine SDKs retain their own licenses.

## External documentation citations

- Epic Games, Unreal Engine FBX Content Pipeline: https://dev.epicgames.com/documentation/en-us/unreal-engine/fbx-content-pipeline
- Unity, AssetPostprocessor: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetPostprocessor.html
- Tether WDK: https://wdk.tether.io/
- WalletConnect Specifications: https://github.com/WalletConnect/walletconnect-specs
- Wallet Standard: https://github.com/wallet-standard/wallet-standard
- Uniswap Smart Order Router: https://github.com/Uniswap/smart-order-router
- OpenGameArt: https://opengameart.org/
- Poly Haven license: https://polyhaven.com/license
- Poly Haven API: https://api.polyhaven.com/
