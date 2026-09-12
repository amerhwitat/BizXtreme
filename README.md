# BizXtreme

BizXtreme is the extended BizX application/game repository, including WebGL/Three.js, Unity/C#, wallet, crypto, game, Aurora, and Chimera integration material.

## Language-separated implementations

- `desktop/vcpp/` — standalone native Visual C++ Windows desktop implementation.
- `desktop/dotnet/` — standalone C# WPF Windows desktop implementation targeting `net48` and `net6.0-windows`.
- `nodejs/` — Node.js implementation.
- `java/` — Java implementation.
- `python/` — Python implementation.
- `javascript/` — browser JavaScript implementation.
- `typescript/` — TypeScript implementation.
- `web/` — browser/WebGL application material.
- `Assets/` — existing Unity/C# application assets and packaged resources.
- `threejs/` — existing Three.js implementation.
- `docs/` — language-neutral architecture and integration documentation.
- `chimera/` — shared 128D/P2P interoperability contracts.

Source implementations are separated by programming language. The new native VC++ and WPF desktop applications are independent source trees and do not mix C++ and C# implementation files.

## Chimera multidimensional integration

BizXtreme uses the Chimera multidimensional application-state model: geometry, time, observer/perspective, light/material response, events, objects, properties, interactions, and extensible cognitive/vector state. The 128D base can be extended without changing the interoperability envelope.

## Peer-to-peer integration

`chimera/p2p_protocol.json` defines authenticated peer identity, capability exchange, request/response and publish/subscribe, sequence/replay controls, content-addressed synchronization, and local-first operation. Discovery is limited to configured/bootstrap peers; arbitrary Internet scanning is not part of the application protocol.

## Standalone Windows desktop editions

### VC++

Open `desktop/vcpp/BizXtremeDesktop.sln` in Visual Studio. The application is C++20/MSVC v143, Unicode, x64, and implements an independent Aurora Frontier dashboard with story progression, score, XP, expedition progress, save/resume, Hall of Fame, and privacy-preserving player discovery.

### C# / WPF

Open `desktop/dotnet/BizXtreme.Desktop.sln`. The project targets `net48` and `net6.0-windows`; the .NET 6 target is configured for x64 self-contained single-file publishing.

Microsoft terminology is preserved: `net6.0` is modern .NET 6, while .NET Framework uses targets such as `net48`. There is no “.NET Framework 6.0” TFM.

See [`docs/DESKTOP_CPP_AND_DOTNET.md`](docs/DESKTOP_CPP_AND_DOTNET.md).

## Existing runtime entry points

| Runtime | Entry point |
|---|---|
| VC++ desktop | `desktop/vcpp/BizXtremeDesktop.cpp` |
| C# desktop | `desktop/dotnet/BizXtreme.Desktop/MainWindow.xaml` |
| Node.js | `nodejs/src/game/launcher.js` |
| Java | `java/src/main/java/io/amerhwitat/bizxtreme/GameLauncher.java` |
| Python | `python/bizxtreme/game_launcher.py` / `python/bizxtreme/__main__.py` |
| Browser JavaScript | `javascript/` / `web/` |
| TypeScript | `typescript/` |
| Unity/C# | `Assets/` |

## License

Released under the GNU General Public License v3 or later for original project code. Existing third-party components retain their original licenses; see their notices. See `LICENSE` where provided.

The new desktop applications complement rather than replace the existing implementations.
