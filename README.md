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

Source implementations are separated by programming language. The new native VC++ and WPF desktop applications are independent source trees and do not mix C++ and C# implementation files.

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

The new desktop applications complement rather than replace the existing implementations.
