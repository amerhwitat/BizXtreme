# BizXtreme Node.js

Node.js 20+ implementation of BizXtreme services and integration boundaries for wallet, crypto, WebGL/Three.js, game, Aurora, and Chimera-facing components.

## Single-point game entry

The canonical Node.js launcher is `src/game/launcher.js`. `npm start` delegates directly to this launcher, providing one runtime-specific command to start the BizXtreme application.

```bash
cd nodejs
npm start
```

An optional mode can be supplied:

```bash
npm start -- arcade
```

Programmatic consumers can import the same launcher boundary:

```js
import { startGame } from '@amerhwitat/bizxtreme/game';

const result = startGame({ mode: 'default' });
```

## Test

```bash
npm test
```

## Language matrix

- `nodejs/` — Node.js 20+ server/integration runtime.
- `java/` — Java 17+ Maven implementation.
- `python/` — Python 3.10+ implementation.
- `javascript/` — browser JavaScript.
- `typescript/` — TypeScript.
- `Assets/` — Unity/C# application assets and packaged resources.

## Node.js layout

- `src/core` — BizXtreme core
- `src/wallet` — wallet/provider boundary
- `src/game/launcher.js` — single-point game/application entry
- `src/crypto` — crypto integration boundary
- `src/webgl` — WebGL capability boundary
- `src/threejs` — Three.js integration boundary
- `src/index.js` — public Node.js API
- `test` — Node.js tests

Packaged APK/WebGL artifacts remain separate from source. Node.js is a first-class server/integration implementation; Java and Python are maintained in their own language-specific trees. See `../docs/GAME_ENTRYPOINTS.md` for the cross-language launcher contract.
