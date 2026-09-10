# BizXtreme Python Architecture

The Python implementation mirrors BizXtreme service boundaries for automation, integration and research workflows.

## Layers

1. `bizxtreme.game_launcher` — single application/game start point.
2. `bizxtreme.core` — runtime identity and health.
3. `bizxtreme.wallet` — provider/JSON-RPC boundary.
4. `bizxtreme.crypto` — chain and coin registry.
5. `bizxtreme.webgl` — browser graphics capability boundary.
6. `bizxtreme.threejs` — Three.js adapter boundary.
7. `bizxtreme.game` — save/state service.
8. `bizxtreme.api` — public facade.
9. `bizxtreme.cli` — command-line utilities.

## Launch flow

`python -m bizxtreme` enters through `bizxtreme.__main__`, which delegates to `bizxtreme.game_launcher.main()`. The launcher creates the public `BizXtremeApi` boundary and leaves game, crypto, wallet, graphics and integration behavior in their native package layers.

```text
python -m bizxtreme
    -> bizxtreme.__main__
        -> bizxtreme.game_launcher.main()
            -> BizXtremeApi
                -> Core / Wallet / Crypto / WebGL / Three.js / Game
```

Python does not claim to replace browser WebGL or Unity rendering; those remain runtime-specific adapters.
