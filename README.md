# BizXtreme

BizXtreme is the extended BizX application/game repository, including WebGL/Three.js, Unity/C#, wallet, crypto, game, Aurora, Chimera integration, Kotlin mobile and Flutter mobile material.

## Unified build and configuration automation

BizXtreme now includes one native build/dependency layer for the full multi-language tree:

```text
build.cmd / build.sh             # build all discoverable applications
install-deps.cmd / install-deps.sh
clean.cmd / clean.sh
scripts/build.ps1 / scripts/build.sh
scripts/install-deps.ps1 / scripts/install-deps.sh
scripts/clean.ps1 / scripts/clean.sh
```

The orchestrator discovers native manifests and dispatches to Node.js/npm, Python/pip, Rust/Cargo, Go/modules, Java/Maven, Kotlin/Gradle, C/C++/CMake, Swift/SwiftPM, Dart/pub, PHP/Composer and Ruby/Bundler. It skips `.git` and generated dependency/build trees, preserves lockfiles, records failures, and returns a non-zero aggregate exit code when builds fail.

The dependency bootstrap installs project dependencies from their native manifests. Missing system toolchains are reported rather than silently installing privileged OS packages. This keeps workstation configuration explicit while still making application dependency setup reproducible.

`.github/workflows/build-all.yml` invokes the same entry points on Linux, Windows and macOS. GitHub provides native CI patterns for the supported ecosystems and dependency-cache integrations. citeturn0search1turn0search5 CMake Presets are supported by CMake for sharing reproducible configure/build settings. citeturn0search0

## Tycoon Business Game

BizXtreme carries the same cross-language Tycoon business engine as BizX: business acquisition, revenue/cost simulation, turn progression, snapshots, shared payment-routing policy, and the provider-neutral monetization engine. Node.js, Java 17 and Python implementations live in their respective language trees and are exposed through their existing single entry points.

All in-game purchase settlement is configured for the primary Ethereum receiving address `0x0B4fF3fc6AE19fAF9A0d2628a646ABD9636B1162`. No private keys are stored in the repository. Real transfers, swaps, and exchanges require explicit user/wallet authorization.

## Monetization

`games/monetization/` adds consumable packs, premium unlocks, subscriptions, banner/interstitial/rewarded ads, revenue events, entitlement tracking, test mode, and server-side verification hooks.

## Free world maps, audio and VFX

`game-assets/` contains the free-asset catalog and machine-readable manifest replacing generated-art dependency.

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
| Payment configuration | [games/payment-config/](games/payment-config/) |
| Monetization | [games/monetization/](games/monetization/) |
| Kotlin mobile | [mobile/kotlin/](mobile/kotlin/) |
| Flutter mobile | [mobile/flutter/](mobile/flutter/) |
| P2P/presence policy | [network/](network/) |
| Node.js | [nodejs/](nodejs/) |
| Java | [java/](java/) |
| Python | [python/](python/) |
| JavaScript / TypeScript | [javascript/](javascript/) / [typescript/](typescript/) |
