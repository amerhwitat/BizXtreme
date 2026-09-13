# BizXtreme

BizXtreme is the extended BizX application/game repository, including WebGL/Three.js, Unity/C#, wallet, crypto, game, Aurora, Chimera integration, Kotlin mobile and Flutter mobile material.

## Tycoon Business Game

BizXtreme carries the same cross-language Tycoon business engine as BizX: business acquisition, revenue/cost simulation, turn progression, snapshots, shared payment-routing policy, and the new provider-neutral monetization engine. Node.js, Java 17 and Python implementations live in their respective language trees and are exposed through their existing single entry points.

All in-game purchase settlement is configured for the primary Ethereum receiving address `0x0B4fF3fc6AE19fAF9A0d2628a646ABD9636B1162`. No private keys are stored in the repository. Real transfers, swaps, and exchanges require explicit user/wallet authorization.

## Monetization

`games/monetization/` adds consumable packs, premium unlocks, subscriptions, banner/interstitial/rewarded ads, revenue events, entitlement tracking, test mode, and server-side verification hooks. Provider targets include Unity Ads/LevelPlay, AppLovin MAX, Google AdMob, Google Play Billing, Apple StoreKit/App Store Connect, and RevenueCat. Provider account IDs and secrets are injected at deployment time and are never committed.

- Configuration: `games/monetization/monetization.json`
- Platform links: `games/monetization/PLATFORM_LINKS.md`
- Integration guide: `games/monetization/README.md`
- Payment configuration: `games/payment-config/`

## Free world maps, audio and VFX

`game-assets/` contains the free-asset catalog and machine-readable manifest replacing generated-art dependency. Realistic environments prioritize CC0 Poly Haven PBR/HDRI/3D assets; nostalgic worlds prioritize CC0 Kenney/OpenGameArt map, cartography and minimap assets. CC0 audio and VFX packs cover UI, ambience, terrain, commerce, machinery, impacts, particles, fire, water, portals and retro effects.

## Source-code citation index

| Area | Source |
|---|---|
| Windows Visual C++ | [desktop/vcpp/](desktop/vcpp/) |
| Windows C# / WPF | [desktop/dotnet/](desktop/dotnet/) |
| Unity 3D C# package | [Unity3D/](Unity3D/) |
| Portable 3D assets | [3D/assets/](3D/assets/) |
| Free game asset catalog | [game-assets/](game-assets/) |
| Realtime rendering | [rendering/](rendering/) |
| Multi-chain crypto | [crypto/](crypto/) |
| Game/store/storyboards | [game-store/](game-store/) |
| Card games & T-Rex | [docs/CARD_GAMES_AND_TREX.md](docs/CARD_GAMES_AND_TREX.md) |
| Payment configuration | [games/payment-config/](games/payment-config/) |
| Monetization | [games/monetization/](games/monetization/) |
| Public release landing page | [docs/index.md](docs/index.md) |
| Kotlin mobile | [mobile/kotlin/](mobile/kotlin/) |
| Flutter mobile | [mobile/flutter/](mobile/flutter/) |
| P2P/presence policy | [network/](network/) |
| Node.js | [nodejs/](nodejs/) |
| Java | [java/](java/) |
| Python | [python/](python/) |
| JavaScript / TypeScript | [javascript/](javascript/) / [typescript/](typescript/) |
