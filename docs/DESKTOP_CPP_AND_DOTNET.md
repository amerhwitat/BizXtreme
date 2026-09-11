# BizXtreme Standalone Desktop Implementations

BizXtreme now contains two isolated Windows desktop implementations. Each is maintained in a separate programming-language subtree.

## Native Visual C++

Path: `desktop/vcpp/`

- `BizXtremeDesktop.sln`
- `BizXtremeDesktop.vcxproj`
- `BizXtremeDesktop.cpp`
- Win32 Unicode / C++20 / MSVC v143
- x64 Debug and Release
- local save/resume
- dashboard KPIs for score, XP, expedition, chapter and play time
- Hall of Fame entry point
- opt-in player discovery notice with privacy-preserving peer identifiers

## C# / WPF

Path: `desktop/dotnet/`

- `BizXtreme.Desktop.sln`
- WPF application
- `net48` compatibility target
- `net6.0-windows` target
- x64 self-contained single-file configuration for .NET 6
- local JSON save/resume
- dashboard, story progression, Hall of Fame and player-discovery entry points

There is no target called “.NET Framework 6.0”. Microsoft uses `net6.0` for modern .NET and `net48`/`net481` for .NET Framework. The desktop project therefore uses both `net48` and `net6.0-windows` where appropriate.

## Source separation

```text
BizXtreme/
  desktop/
    vcpp/       # native C++ only
    dotnet/     # C# / WPF only
  Assets/       # existing Unity/C# source and resources
  threejs/      # existing Three.js source
  nodejs/       # existing Node.js source
  java/         # existing Java source
  python/       # existing Python source
```

No C++ source is embedded in the C# desktop project and no C# source is embedded in the native VC++ project.

## Standalone scope

These desktop editions provide a native standalone baseline around BizXtreme's existing game concepts: Aurora Frontier progression, story chapters, KPI dashboard, save/resume, Hall of Fame, and privacy-preserving peer discovery. They do not delete or replace the existing Unity, Three.js, browser, Node.js, Java, or Python implementations.
