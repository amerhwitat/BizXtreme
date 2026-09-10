# BizXtreme Node.js

Node.js implementation of BizXtreme services and integration boundaries for wallet, crypto, WebGL/Three.js, game, Aurora, and Chimera-facing components.

## Requirements
- Node.js 20+

## Run
```bash
npm test
npm start
```

## Layout
- `src/core` — BizXtreme core
- `src/wallet` — wallet/provider boundary
- `src/index.js` — public Node.js API
- `test` — Node.js tests

Packaged APK/WebGL artifacts remain separate from source. Native, browser JavaScript, TypeScript, and other-language implementations are kept in their own language-specific trees.
