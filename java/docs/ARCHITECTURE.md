# BizXtreme Java Architecture

The Java implementation mirrors BizXtreme service boundaries while keeping Java source isolated from Unity/C#, Node.js, Python and browser source.

## Layers

- `core` — runtime identity and health.
- `wallet` — provider/JSON-RPC boundary.
- `crypto` — chain and coin registry.
- `webgl` — browser graphics capability boundary.
- `threejs` — Three.js adapter boundary.
- `game` — save/state service.
- `api` — public facade.

Java does not attempt to replace the browser WebGL runtime or Unity renderer; those remain runtime-specific integrations.
