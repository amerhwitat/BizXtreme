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

## Build and run

Use the unified build layer first:

```bat
build-tools\build.bat
```

or:

```powershell
.\build-tools\build.ps1
```

### VC++ desktop

Open `desktop/vcpp/BizXtremeDesktop.sln` in Visual Studio and select `Release|x64`, or use the repository MSVC wrapper.

### C# / WPF

```powershell
dotnet build desktop\dotnet\BizXtreme.Desktop.sln -c Release
```

### Node.js

```bash
cd nodejs && npm ci && npm test
node src/game/launcher.js
```

### Java

```bash
cd java && mvn test
```

### Python

```bash
python -m pip install -r python/requirements.txt
python python/bizxtreme/game_launcher.py
```

### Web / Three.js

Enter `web/` or `threejs/`, install the declared package-manager dependencies and run the package's documented development/build script. Do not mix the browser runtime with the desktop source tree.

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

The desktop applications complement rather than replace the existing implementations.
