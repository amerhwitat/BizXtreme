# BizXtreme Game/Application Entry Points

BizXtreme exposes a single native start point for each implemented runtime. The launchers are intentionally thin and delegate into the runtime's existing API/core and game-related services.

## Entry-point matrix

| Runtime | Entry point | Command |
|---|---|---|
| Node.js 20+ | `nodejs/src/game/launcher.js` | `cd nodejs && npm start` |
| Java 17+ | `java/src/main/java/io/amerhwitat/bizxtreme/GameLauncher.java` | `cd java && mvn package && java -cp target/classes io.amerhwitat.bizxtreme.GameLauncher` |
| Python 3.10+ | `python/bizxtreme/game_launcher.py` via `python/bizxtreme/__main__.py` | `cd python && python -m bizxtreme` |
| Browser JavaScript | `javascript/` / `web/` runtime entry | See browser application documentation |
| TypeScript | `typescript/` runtime entry | See TypeScript application documentation |
| Unity/C# | `Assets/` application entry | See Unity project documentation |

## Design contract

1. Each language/runtime owns its own launcher.
2. A launcher imports only its language-native implementation.
3. The launcher delegates into the public API/core boundary rather than duplicating business logic.
4. Runtime-specific arguments remain native to that runtime.
5. Packaged APK/WebGL artifacts remain build outputs/assets, not alternate source-language implementations.

## Node.js

`npm start` is the canonical Node.js application/game start command. The launcher is also exported through the `./game` package subpath.

```js
import { startGame } from '@amerhwitat/bizxtreme/game';

startGame({ mode: 'default' });
```

## Java

`io.amerhwitat.bizxtreme.GameLauncher` is the canonical JVM entry class.

```bash
mvn package
java -cp target/classes io.amerhwitat.bizxtreme.GameLauncher
```

## Python

`bizxtreme.__main__` delegates to `bizxtreme.game_launcher.main()`, making the package command the canonical Python entry.

```bash
python -m bizxtreme
```

The launcher can also be invoked as a module:

```bash
python -m bizxtreme.game_launcher
```

## Runtime boundaries

The Java and Python implementations provide application/service boundaries, while Node.js provides the server/integration runtime. Browser JavaScript, TypeScript and Unity/C# remain responsible for their respective rendering/application environments. Crypto, wallet, WebGL/Three.js, save/state, Aurora and Chimera integrations stay behind their runtime-native boundaries.
