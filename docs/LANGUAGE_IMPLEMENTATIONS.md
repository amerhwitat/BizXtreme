# BizXtreme Language Implementations

BizXtreme maintains parallel implementations with mirrored service boundaries while preserving runtime-specific behavior.

| Language/runtime | Directory | Purpose |
|---|---|---|
| Node.js 20+ | `nodejs/` | Server and web/API integration |
| Java 17+ | `java/` | JVM services and integration |
| Python 3.10+ | `python/` | Automation, tooling and service integration |
| Browser JavaScript | `javascript/` | Browser/WebGL-facing implementation |
| TypeScript | `typescript/` | Typed browser/application implementation |
| Unity/C# | `Assets/Scripts/` | Existing Unity application runtime |

## Separation rule

Java and Python source is isolated under `java/` and `python/`. Browser and Unity source remain in their existing runtime-specific trees. Packaged APK/WebGL files remain artifacts.

## Common boundaries

The language implementations share conceptual boundaries for core runtime state, wallet/provider requests, crypto/chain registries, WebGL/Three.js adapters, game state, APIs, Aurora integration and Chimera integration. A boundary may be implemented differently per runtime; it must not be represented as foreign-language source.

## Verification

Node.js uses `npm test`; Java uses `mvn test`; Python uses `python -m unittest discover -s tests`. Unity/C# continues to use the Unity build/test pipeline.
