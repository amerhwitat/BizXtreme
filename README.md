# BizXtreme

BizXtreme is the extended BizX application/game repository, including WebGL/Three.js, Unity/C#, wallet, crypto, game, Aurora, Chimera integration and Kotlin mobile material.

## Source-code citation index

| Area | Source |
|---|---|
| Windows Visual C++ | [desktop/vcpp/](desktop/vcpp/) |
| Windows C# / WPF | [desktop/dotnet/](desktop/dotnet/) |
| Node.js | [nodejs/](nodejs/) |
| Java | [java/](java/) |
| Python | [python/](python/) |
| JavaScript | [javascript/](javascript/) |
| TypeScript | [typescript/](typescript/) |
| Web | [web/](web/) |
| Three.js/WebGL | [threejs/](threejs/) |
| Unity/C# | [Assets/](Assets/) |
| Kotlin mobile | [kotlin/mobile/](kotlin/mobile/) |
| Apple/Swift | [apple/](apple/) |
| Chimera integration | [chimera/](chimera/) |
| Aurora integration | [aurora_integration.json](aurora_integration.json) |
| Documentation | [docs/](docs/) |
| Complete repository source tree | [all tracked source](.) |

The links above are the README-level citations for the maintained code; language/component READMEs provide deeper file-level inventories.

## Language-separated implementations

- `desktop/vcpp/` — standalone native Visual C++ Windows desktop implementation.
- `desktop/dotnet/` — standalone C# WPF Windows desktop implementation.
- `nodejs/`, `java/`, `python/`, `javascript/`, `typescript/`, `web/`, `Assets/`, `threejs/` — runtime/application implementations.
- `kotlin/mobile/` — Android Kotlin mobile application.
- `apple/` — iOS/iPadOS and macOS SwiftUI/Xcode source boundary.
- `docs/` — language-neutral architecture and integration documentation.

## Mobile communications

BizXtreme Mobile uses the shared conversation contract with BizX: conversation ID, sender ID, monotonic sequence and SHA-256 payload integrity. It provides microphone/speaker/camera capability detection and a WebRTC media boundary for synchronized voice/video sessions. Runtime permissions are requested at the point of user action. See `kotlin/mobile/COMMUNICATIONS.md`.

BizXtreme is the second primary integration target for synchronized IRC-style channels, presence, voice/video sessions and shared application/game conversation state.

## Apple applications

`apple/project.yml` is an XcodeGen specification for iOS and macOS application targets. `apple/Sources/` contains the SwiftUI entry point and application boundary. The centralized Objective-C and Flutter companion is maintained in [`general/Apple-Implementations/BizXtreme`](https://github.com/amerhwitat/general/tree/master/Apple-Implementations/BizXtreme). On macOS, install Xcode/XcodeGen, generate the project, then build/archive/export. Signing material stays outside Git.

## Standalone Windows desktop editions

Open `desktop/vcpp/BizXtremeDesktop.sln` for VC++ or `desktop/dotnet/BizXtreme.Desktop.sln` for WPF.

## Chimera 128D + authenticated P2P

BizXtreme participates in the shared Chimera multidimensional application fabric. The optional P2P layer is authenticated and opt-in and supports capability exchange, request/response, pub/sub, snapshot/delta synchronization, content-addressed state, sequence numbers and payload integrity. It excludes unsolicited scanning, credential exchange, arbitrary executable transfer and remote command execution.

## Mobile build

Use `ChimeraIIOS/tools/mobile/` to provision the Android SDK and build debug/release APKs across the portfolio.

## Licensing

New and modified BizXtreme code is intended for GNU GPL v3 or later. Third-party assets and dependencies retain their own licenses.
