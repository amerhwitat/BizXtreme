# BizXtreme

BizXtreme is the extended BizX application/integration repository, including WebGL/Three.js, wallet, crypto, game, Aurora, and Chimera integration material.

## Language-separated implementations

- `nodejs/` — Node.js 20+ server/integration implementation.
- `java/` — Java 17+ implementation using Maven.
- `python/` — Python 3.10+ implementation.
- `javascript/` — browser JavaScript implementation where applicable.
- `typescript/` — TypeScript implementation where applicable.
- `web/` — browser/WebGL application material.
- `Assets/` — Unity/C# application assets and packaged resources.
- `docs/` — language-neutral architecture and integration documentation.

Source implementations are separated by programming language. Packaged APK/WebGL artifacts remain artifacts and are not represented as Java, Python, or Node.js source.

## Single-point game entry

Each supported runtime has a language-native game/application launcher. The launcher starts BizXtreme through that runtime's public API/core boundary while keeping language-specific source isolated.

| Runtime | Single entry point | Start command |
|---|---|---|
| Node.js 20+ | `nodejs/src/game/launcher.js` | `npm start` from `nodejs/` |
| Java 17+ | `java/src/main/java/io/amerhwitat/bizxtreme/GameLauncher.java` | `java -cp target/classes io.amerhwitat.bizxtreme.GameLauncher` after `mvn package` |
| Python 3.10+ | `python/bizxtreme/game_launcher.py` / `python/bizxtreme/__main__.py` | `python -m bizxtreme` from `python/` |
| Browser JavaScript | language-native browser entry | see `javascript/` / `web/` documentation |
| TypeScript | language-native application entry | see `typescript/` documentation |
| Unity/C# | Unity application entry | see `Assets/` documentation |

See [`docs/GAME_ENTRYPOINTS.md`](docs/GAME_ENTRYPOINTS.md) for the complete launcher contract and runtime matrix.

## Node.js

```bash
cd nodejs
npm test
npm start
```

## Java

```bash
cd java
mvn test
mvn package
java -cp target/classes io.amerhwitat.bizxtreme.GameLauncher
```

## Python

```bash
cd python
python -m unittest discover -s tests
python -m bizxtreme
```

Java and Python provide native application/service boundaries while Node.js provides the server/web integration foundation. Browser, TypeScript, Unity/C#, and packaged application material remain in their appropriate language/runtime trees.
