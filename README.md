# BizXtreme

BizXtreme is the extended BizX application/game repository, including WebGL/Three.js, Unity/C#, wallet, crypto, game, Aurora, Chimera integration, Kotlin mobile and Flutter mobile material.

## Web search tags

**Core tags:** `bizxtreme`, `game-platform`, `game-engine`, `unified-game`, `business-simulation`, `tycoon-game`, `rpg`, `strategy-game`, `webgl`, `threejs`, `unity`, `csharp`, `networking`, `p2p`, `multiplayer`, `crypto`, `crypto-wallet`, `blockchain`, `asset-browser`, `python`, `nodejs`, `java`, `rust`, `go`, `cpp`, `typescript`, `kotlin`, `flutter`, `mobile-game`, `cross-platform`, `ai`, `rendering`

**Search phrases:** BizXtreme game platform, unified cross-platform game application, business simulation game engine, tycoon game platform, WebGL Three.js game engine, Unity C# game systems, multiplayer P2P networking, cross-language game development, cryptocurrency wallet integration, open licensed game asset browser, mobile game Kotlin Flutter, real-time game rendering, AI game systems, cross-platform game networking.

See `WEB_SEARCH_TAGS.md` for the maintained tag set and search-phrase metadata.

## Unified Game Application

`UnifiedGame/` provides a single runnable application facade that combines the game, economy, virtual crypto-asset simulation, rendering capability adapters and networking/session concepts while preserving existing native implementations.

## NetworkUnified — user-facing networking/API application

`NetworkUnified/` consolidates networking/API functionality behind the versioned `bizxtreme.network.api.v1` contract. Runnable implementations are provided for Python, Node.js, TypeScript, Go, Rust, Java, C#, C++, Dart, Kotlin, Swift, PHP and Ruby.

## AssetBrowser — in-game open/free asset library

`AssetBrowser/` provides the game-facing GUI for searching openly licensed images/audio and curated CC0 game/3D assets, inspecting license/provenance information, downloading selected assets, verifying SHA-256, and importing them into `game_assets/`. Providers are Openverse, Poly Haven and the official Kenney catalog. Downloads are restricted to configured HTTPS provider hosts and are never executed. Every imported asset is recorded in `game_assets/manifest.json`.

Run `AssetBrowser/scripts/run.bat`, `AssetBrowser/scripts/run.ps1`, or `AssetBrowser/scripts/run.sh`; the default local GUI/API address is `http://127.0.0.1:8790`.

Public active network targets remain allowlist-only. The network layer does not implement Internet-wide enumeration, credential attacks, evasion, spoofing, or exploitation.

## Unified build and configuration automation

BizXtreme provides repository-level build/dependency automation through `build.cmd`, `build.sh`, `install-deps.cmd`, `install-deps.sh`, `clean.cmd`, `clean.sh`, and the corresponding PowerShell/POSIX scripts under `scripts/`. Missing system toolchains are reported rather than silently installing privileged OS packages.

## Tycoon Business Game

BizXtreme carries the cross-language Tycoon business engine: business acquisition, revenue/cost simulation, turn progression, snapshots, shared payment-routing policy, and provider-neutral monetization.

## Monetization

`games/monetization/` adds consumable packs, premium unlocks, subscriptions, ads, revenue events, entitlement tracking, test mode, and server-side verification hooks.

## Source-code index

| Area | Source |
|---|---|
| Unified application | [UnifiedGame/](UnifiedGame/) |
| Network API | [NetworkUnified/](NetworkUnified/) |
| Asset Browser | [AssetBrowser/](AssetBrowser/) |
| Visual C++ Windows | [desktop/vcpp/](desktop/vcpp/) |
| C# / WPF | [desktop/dotnet/](desktop/dotnet/) |
| Unity 3D | [Unity3D/](Unity3D/) |
| Rendering | [rendering/](rendering/) |
| Crypto | [crypto/](crypto/) |
| Mobile Kotlin | [mobile/kotlin/](mobile/kotlin/) |
| Flutter | [mobile/flutter/](mobile/flutter/) |
| P2P/presence | [network/](network/) |
| Node.js | [nodejs/](nodejs/) |
| Java | [java/](java/) |
| Python | [python/](python/) |
| JavaScript / TypeScript | [javascript/](javascript/) / [typescript/](typescript/) |
