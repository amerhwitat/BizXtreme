# BizXtreme Game/Application Entry Points

BizXtreme exposes a native start point for each implemented runtime. Source remains separated by language/runtime.

## Entry-point matrix

| Runtime | Entry point | Command |
|---|---|---|
| Native VC++ | `desktop/vcpp/BizXtremeDesktop.cpp` | Open `desktop/vcpp/BizXtremeDesktop.sln` and Build x64 |
| C# / WPF | `desktop/dotnet/BizXtreme.Desktop/MainWindow.xaml` | Open `desktop/dotnet/BizXtreme.Desktop.sln` and Build x64 |
| Node.js | `nodejs/src/game/launcher.js` | `cd nodejs && npm start` |
| Java | `java/src/main/java/io/amerhwitat/bizxtreme/GameLauncher.java` | `cd java && mvn package && java -cp target/classes io.amerhwitat.bizxtreme.GameLauncher` |
| Python | `python/bizxtreme/game_launcher.py` via `python/bizxtreme/__main__.py` | `cd python && python -m bizxtreme` |
| Browser JavaScript | `javascript/` / `web/` runtime entry | See browser documentation |
| TypeScript | `typescript/` runtime entry | See TypeScript documentation |
| Unity/C# | `Assets/` application entry | See Unity documentation |

## Desktop targets

The C# desktop solution uses `net48` plus `net6.0-windows`. Modern .NET 6 is represented by `net6.0`; .NET Framework uses targets such as `net48`. “.NET Framework 6.0” is not a valid TFM.

The native VC++ edition is a standalone Win32 Unicode x64 application using C++20/MSVC v143. The C# edition is a standalone WPF application with self-contained single-file publishing configured for Windows x64 on the .NET 6 target.

## Design contract

1. Each language/runtime owns its launcher.
2. C++ and C# desktop implementations do not share source files.
3. Existing Node.js, Java, Python, browser, TypeScript and Unity implementations remain independently maintained.
4. Runtime-specific arguments remain native to that runtime.
5. Documentation and build metadata stay synchronized.
