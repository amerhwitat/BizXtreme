# BizXtreme Language Implementations

BizXtreme maintains parallel implementations with mirrored service boundaries while preserving runtime-specific behavior and a consistent single-point application launch contract.

| Language/runtime | Directory | Purpose | Game/application entry |
|---|---|---|---|
| Node.js 20+ | `nodejs/` | Server and web/API integration | `src/game/launcher.js` / `npm start` |
| Java 17+ | `java/` | JVM services and integration | `io.amerhwitat.bizxtreme.GameLauncher` |
| Python 3.10+ | `python/` | Automation, tooling and service integration | `python -m bizxtreme` |
| Browser JavaScript | `javascript/` | Browser/WebGL-facing implementation | language-native browser entry |
| TypeScript | `typescript/` | Typed browser/application implementation | language-native application entry |
| Unity/C# | `Assets/Scripts/` | Existing Unity application runtime | Unity application entry |

## Single-point launch contract

Each language/runtime owns its own launcher and delegates into its native public API/core and game boundary. Launchers do not import source from another programming-language tree. Runtime-specific rendering and platform behavior remains in the appropriate runtime.

Implemented server/service launchers:

- Node.js: `nodejs/src/game/launcher.js`, wired to `npm start`.
- Java: `java/src/main/java/io/amerhwitat/bizxtreme/GameLauncher.java`.
- Python: `python/bizxtreme/game_launcher.py`, exposed as `python -m bizxtreme` through `python/bizxtreme/__main__.py`.

Browser JavaScript, TypeScript and Unity/C# retain their runtime-native application entry mechanisms.

## Separation rule

Java and Python source is isolated under `java/` and `python/`. Browser and Unity source remain in their existing runtime-specific trees. Packaged APK/WebGL files remain artifacts.

## Common boundaries

The language implementations share conceptual boundaries for core runtime state, wallet/provider requests, crypto/chain registries, WebGL/Three.js adapters, game state, APIs, Aurora integration and Chimera integration. A boundary may be implemented differently per runtime; it must not be represented as foreign-language source.

## Verification

Node.js uses `npm test`; Java uses `mvn test`; Python uses `python -m unittest discover -s tests`; launcher smoke commands are documented in `GAME_ENTRYPOINTS.md`. Unity/C# continues to use the Unity build/test pipeline.
