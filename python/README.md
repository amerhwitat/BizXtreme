# BizXtreme Python

Python 3.10+ implementation of BizXtreme integration services.

## GUI-first entry

The canonical interactive entry point is now the native Tkinter application:

```bash
cd python
python -m bizxtreme
```

The GUI provides mode selection, live status and diagnostics while keeping the reusable engine available through `bizxtreme.game_launcher.main()` for tests, automation and headless workflows.

Direct headless engine use:

```bash
python -m bizxtreme.game_launcher
```

## Requirements

```bash
python -m pip install -r requirements.txt
```

Tkinter is supplied by supported desktop Python distributions; Linux users may need their distribution's Tk package.

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
- `bizxtreme/game_launcher.py` — reusable headless engine entry
- `bizxtreme/gui.py` — native GUI application entry
- `bizxtreme/__main__.py` — GUI-first package entry
- `tests` — standard-library tests

Python source remains isolated here; Unity/C#, browser assets, JavaScript/TypeScript, Node.js and mobile artifacts remain in their respective trees.
