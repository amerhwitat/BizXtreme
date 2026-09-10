# BizXtreme Node.js

Node.js 20+ implementation of BizXtreme services and integration boundaries for wallet, crypto, WebGL/Three.js, game, Aurora, and Chimera-facing components.

## Run and test

```bash
npm test
npm start
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
- `src/index.js` — public Node.js API
- `test` — Node.js tests

Packaged APK/WebGL artifacts remain separate from source. Node.js is a first-class server/integration implementation; Java and Python are maintained in their own language-specific trees.
