# BizXtreme Java

Java 17+ implementation of BizXtreme services and integration boundaries.

## Single-point game entry

`io.amerhwitat.bizxtreme.GameLauncher` is the canonical Java entry point for starting the BizXtreme game/application runtime. It creates the public `BizXtremeApi` boundary and keeps the launcher independent of Unity/C#, Node.js, Python, and browser source.

Build and launch:

```bash
mvn package
java -cp target/classes io.amerhwitat.bizxtreme.GameLauncher
```

## Build and test

```bash
mvn test
```

## Layout

- `src/main/java/io/amerhwitat/bizxtreme/GameLauncher.java` — single-point game/application entry
- `core` — runtime/core model
- `wallet` — wallet provider / JSON-RPC boundary
- `crypto` — chain/coin registry boundary
- `webgl` — WebGL runtime boundary
- `threejs` — Three.js integration boundary
- `game` — save/state service
- `api` — public API boundary
- `src/test/java` — JUnit tests

Unity/C# and packaged APK/WebGL artifacts remain in their existing application trees; this Java directory contains Java only. See `../docs/GAME_ENTRYPOINTS.md` for the cross-language launcher contract.
