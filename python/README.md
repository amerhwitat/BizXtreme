# BizXtreme Python

Python 3.10+ implementation of BizXtreme integration services.

## Single-point game entry

The canonical Python launcher is `bizxtreme.game_launcher.main()`. The package module entry `python -m bizxtreme` delegates to the same function, giving Python consumers one application start path.

```bash
cd python
python -m bizxtreme
```

The launcher can also be invoked as a module:

```bash
python -m bizxtreme.game_launcher
```

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
- `bizxtreme/cli` — command-line utilities
- `bizxtreme/game_launcher.py` — single-point game/application entry
- `bizxtreme/__main__.py` — package entry delegating to the launcher
- `tests` — standard-library tests

Python source is isolated here. Unity/C#, browser assets, JavaScript/TypeScript, Node.js, and packaged APK/WebGL artifacts remain in their respective application trees. See `../docs/GAME_ENTRYPOINTS.md` for the cross-language launcher contract.
