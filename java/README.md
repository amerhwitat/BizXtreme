# BizXtreme Java

Java 17+ implementation of BizXtreme services and integration boundaries.

## Build and test

```bash
mvn test
```

## Layout

- `core` — runtime/core model
- `wallet` — wallet provider / JSON-RPC boundary
- `crypto` — chain/coin registry boundary
- `webgl` — WebGL runtime boundary
- `threejs` — Three.js integration boundary
- `game` — save/state service
- `api` — public API boundary
- `src/test/java` — JUnit tests

Unity/C# and packaged APK/WebGL artifacts remain in their existing application trees; this Java directory contains Java only.
