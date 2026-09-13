# BizXtreme

BizXtreme is the extended BizX application/game repository, including WebGL/Three.js, Unity/C#, wallet, crypto, game, Aurora, Chimera integration, Kotlin mobile and Flutter mobile material.

## Unified Game Application

`UnifiedGame/` provides a single runnable application facade that combines the game, economy, virtual crypto-asset simulation, rendering capability adapters and networking/session concepts while preserving the existing native implementations.

Quick start from `UnifiedGame/`:

```text
scripts/setup.ps1
scripts/run.ps1 -Mode tycoon
```

POSIX: `./scripts/setup.sh && ./scripts/run.sh --mode tycoon`

Windows CMD: `scripts\setup.bat` then `scripts\run.bat --mode tycoon`

Build available native adapters with `scripts/build.ps1`, `scripts/build.sh`, or `scripts/build.bat`.

### Unified subsystems

- Game: Tycoon, sandbox, multiplayer/session and progression adapters
- Economy: virtual cash/assets and progression
- Crypto: provider-neutral in-game coin/wallet simulation; no private keys
- Rendering: Unity, WebGL/Three.js and native renderer integration points
- Networking: local/offline and existing network-session integration points
- Runtimes: Node.js, Python, Java, C++, Rust, Go, C#, TypeScript, plus existing repository implementations

The existing language-specific projects remain intact. The unified layer is an orchestration/facade rather than a destructive rewrite.

## Unified build and configuration automation

BizXtreme also includes repository-level build/dependency automation:

```text
build.cmd / build.sh
install-deps.cmd / install-deps.sh
clean.cmd / clean.sh
scripts/build.ps1 / scripts/build.sh
scripts/install-deps.ps1 / scripts/install-deps.sh
scripts/clean.ps1 / scripts/clean.sh
```

The orchestrator discovers native manifests and dispatches to Node.js/npm, Python/pip, Rust/Cargo, Go/modules, Java/Maven, Kotlin/Gradle, C/C++/CMake, Swift/SwiftPM, Dart/pub, PHP/Composer and Ruby/Bundler. Missing system toolchains are reported rather than silently installing privileged OS packages.

## Tycoon Business Game

BizXtreme carries the cross-language Tycoon business engine: business acquisition, revenue/cost simulation, turn progression, snapshots, shared payment-routing policy, and provider-neutral monetization. Node.js, Java 17 and Python implementations live in their respective language trees and expose existing single entry points.

All in-game purchase settlement remains subject to explicit wallet authorization. No private keys are stored in the repository.

## Monetization

`games/monetization/` adds consumable packs, premium unlocks, subscriptions, banner/interstitial/rewarded ads, revenue events, entitlement tracking, test mode, and server-side verification hooks.

## Source-code index

| Area | Source |
|---|---|
| Unified application | [UnifiedGame/](UnifiedGame/) |
| Windows Visual C++ | [desktop/vcpp/](desktop/vcpp/) |
| Windows C# / WPF | [desktop/dotnet/](desktop/dotnet/) |
| Unity 3D C# | [Unity3D/](Unity3D/) |
| Portable 3D assets | [3D/assets/](3D/assets/) |
| Realtime rendering | [rendering/](rendering/) |
| Multi-chain crypto | [crypto/](crypto/) |
| Game/store/storyboards | [game-store/](game-store/) |
| Payment configuration | [games/payment-config/](games/payment-config/) |
| Monetization | [games/monetization/](games/monetization/) |
| Kotlin mobile | [mobile/kotlin/](mobile/kotlin/) |
| Flutter mobile | [mobile/flutter/](mobile/flutter/) |
| P2P/presence | [network/](network/) |
| Node.js | [nodejs/](nodejs/) |
| Java | [java/](java/) |
| Python | [python/](python/) |
| JavaScript / TypeScript | [javascript/](javascript/) / [typescript/](typescript/) |
