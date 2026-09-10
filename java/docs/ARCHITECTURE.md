# BizXtreme Java Architecture

The Java implementation mirrors BizXtreme service boundaries while keeping Java source isolated from Unity/C#, Node.js, Python and browser source.

## Layers

1. `GameLauncher` — single application/game start point.
2. `core` — runtime identity and health.
3. `wallet` — provider/JSON-RPC boundary.
4. `crypto` — chain and coin registry.
5. `webgl` — browser graphics capability boundary.
6. `threejs` — Three.js adapter boundary.
7. `game` — save/state service.
8. `api` — public facade.

## Launch flow

`GameLauncher.main()` creates `BizXtremeApi` and starts the Java application boundary. The launcher remains thin so game, crypto, wallet, WebGL/Three.js and integration behavior stay behind their existing service layers.

```text
GameLauncher
    -> BizXtremeApi
        -> Core / Wallet / Crypto / WebGL / Three.js / Game
```

Java does not attempt to replace the browser WebGL runtime or Unity renderer; those remain runtime-specific integrations.
