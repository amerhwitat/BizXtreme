# BizXtreme Python

Python 3.10+ implementation of BizXtreme integration services.

## Test

```bash
python -m unittest discover -s tests
```

## Package layout

- `bizxtreme/core` — runtime/core model
- `bizxtreme/wallet` — wallet provider / JSON-RPC boundary
- `bizxtreme/crypto` — chain/coin registry boundary
- `bizxtreme/webgl` — WebGL runtime boundary
- `bizxtreme/threejs` — Three.js integration boundary
- `bizxtreme/game` — save/state service
- `bizxtreme/api` — public API boundary
- `bizxtreme/cli` — command-line entry point
- `tests` — standard-library tests

Python source is isolated here. Unity/C#, browser assets, JavaScript/TypeScript, Node.js, and packaged APK/WebGL artifacts remain in their respective application trees.
