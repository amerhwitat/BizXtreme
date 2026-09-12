# BizXtreme

BizXtreme is the extended BizX application/game repository, including WebGL/Three.js, Unity/C#, wallet, crypto, game, Aurora, Chimera integration and Kotlin mobile material.

## Language-separated implementations

- `desktop/vcpp/` — standalone native Visual C++ Windows desktop implementation.
- `desktop/dotnet/` — standalone C# WPF Windows desktop implementation.
- `nodejs/`, `java/`, `python/`, `javascript/`, `typescript/`, `web/`, `Assets/`, `threejs/` — existing runtime/application implementations.
- `kotlin/mobile/` — Android Kotlin mobile application.
- `docs/` — language-neutral architecture and integration documentation.

## Mobile communications

BizXtreme Mobile uses the shared conversation contract with BizX: conversation ID, sender ID, monotonic sequence and SHA-256 payload integrity. It provides microphone/speaker/camera capability detection and a WebRTC media boundary for synchronized voice/video sessions. Runtime permissions are requested at the point of user action. See [`kotlin/mobile/COMMUNICATIONS.md`](kotlin/mobile/COMMUNICATIONS.md).

BizXtreme is the second primary integration target for synchronized IRC-style channels, presence, voice/video sessions and shared application/game conversation state.

## Standalone Windows desktop editions

Open `desktop/vcpp/BizXtremeDesktop.sln` for VC++ or `desktop/dotnet/BizXtreme.Desktop.sln` for WPF.

## Chimera 128D + authenticated P2P

BizXtreme participates in the shared Chimera multidimensional application fabric. The optional P2P layer is authenticated and opt-in and supports capability exchange, request/response, pub/sub, snapshot/delta synchronization, content-addressed state, sequence numbers and payload integrity. It excludes unsolicited scanning, credential exchange, arbitrary executable transfer and remote command execution.

## Mobile build

Use `ChimeraIIOS/tools/mobile/` to provision the Android SDK and build debug/release APKs across the portfolio.

## Licensing

New and modified BizXtreme code is intended for GNU GPL v3 or later. Third-party assets and dependencies retain their own licenses.
