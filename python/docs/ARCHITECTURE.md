# BizXtreme Python Architecture

The Python implementation mirrors BizXtreme service boundaries for automation, integration and research workflows.

## Layers

- `bizxtreme.core` — runtime identity and health.
- `bizxtreme.wallet` — provider/JSON-RPC boundary.
- `bizxtreme.crypto` — chain and coin registry.
- `bizxtreme.webgl` — browser graphics capability boundary.
- `bizxtreme.threejs` — Three.js adapter boundary.
- `bizxtreme.game` — save/state service.
- `bizxtreme.api` — public facade.
- `bizxtreme.cli` — command-line entry point.

Python does not claim to replace browser WebGL or Unity rendering; those remain runtime-specific adapters.
