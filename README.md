# BizXtreme

BizXtreme is the extended BizX application/integration repository, including WebGL/Three.js, wallet, crypto, game, Aurora, and Chimera integration material.

## Implementations

- `nodejs/` — Node.js 20+ implementation and server/integration APIs.
- `javascript/` — browser JavaScript implementation where applicable.
- `typescript/` — TypeScript implementation where applicable.
- `web/` — browser/WebGL application material.
- `docs/` — language-neutral architecture and integration documentation.
- `Assets/` — application assets and packaged resources.

Each source implementation is kept under its programming-language directory. Packaged APK/WebGL artifacts are retained as artifacts and are not treated as Node.js source.

## Node.js

```bash
cd nodejs
npm test
npm start
```

Node.js is a first-class implementation and provides the reusable core and wallet/provider boundaries for future API, crypto, WebGL, game, Aurora, and Chimera integrations.
