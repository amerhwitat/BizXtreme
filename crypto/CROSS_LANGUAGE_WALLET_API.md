# BizXtreme Cross-Language Crypto & Wallet API

The crypto subsystem is shared conceptually by every game implementation while remaining native to each language/runtime.

## Modes

- `free`: gameplay and assets work without cryptocurrency.
- `testnet`: wallet/provider operations use development networks or local simulation.
- `mainnet`: disabled by default and requires an explicitly configured provider boundary.

## Supported capability families

- secure hashing and MACs
- public-key signatures and verification
- address/chain validation
- wallet creation, import, watch-only mode and disconnect
- balances and transaction history
- fee/gas estimation
- transaction construction, simulation and provider handoff
- confirmation tracking and replay protection
- QR receive/request workflows
- game economy and marketplace settlement boundaries

## Secret boundary

Raw private keys and seed phrases are never required by the game API. When signing is needed, an external wallet or secure platform keystore/provider should perform the operation. Secrets must never be written to logs, telemetry, crash reports or ordinary configuration files.

## Entitlements

A confirmed provider transaction may trigger a server-side entitlement update. Client-side transaction submission alone never grants a paid game asset.

## Language parity

Node.js/JavaScript/TypeScript, Python, Java, C#, C++, Rust, Go, Kotlin, Dart/Flutter, Swift, PHP and other implementations should expose equivalent capability names while using their ecosystem's secure cryptographic primitives.
