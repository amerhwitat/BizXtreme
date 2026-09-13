# BizXtreme Unified Game

A single runnable application facade over the BizXtreme game, rendering, economy, crypto-asset simulation, networking, and existing language runtimes.

## Architecture

The unified runtime is intentionally provider-neutral:

- `game/` — gameplay/session state
- `economy/` — virtual cash, assets, progression
- `crypto/` — simulated coins/wallet ledger; no private keys
- `rendering/` — renderer capability selection and adapters
- `networking/` — local/offline capability description
- `launcher/` — one entry point per supported language
- `scripts/` — Windows CMD, PowerShell and POSIX automation

The canonical reference implementation is dependency-light Python. Node.js is a first-class runtime and the other language launchers expose the same JSON command contract.

## Run

From `UnifiedGame/`:

```text
python launcher/python/main.py --mode tycoon
node launcher/node/index.js --mode tycoon
```

Or use the repository-level scripts:

```text
scripts/setup.ps1
scripts/run.ps1 -Mode tycoon
```

`setup` reports missing toolchains and does not install privileged OS packages automatically.

## Crypto safety

The crypto subsystem is a game-economy simulation. Coins and balances are not real cryptocurrency, and private keys are never generated or stored by this application. Real-chain settlement remains behind explicit external wallet authorization in the existing BizXtreme integrations.
