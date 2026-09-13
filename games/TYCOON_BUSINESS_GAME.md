# Tycoon Business Game

BizXtreme Tycoon is the extended BizX business/economy runtime, implemented independently in Node.js, Java 17 and Python while remaining compatible with the existing game, wallet, crypto, WebGL and integration layers.

## Included features

- Business acquisition and ownership
- Revenue, operating costs and profit simulation
- Turn-based progression and state snapshots
- Extensible business definitions
- Primary ETH settlement metadata
- Non-custodial wallet authorization boundary

## Payment routing

Primary ETH receiving address: `0x0B4fF3fc6AE19fAF9A0d2628a646ABD9636B1162`

All in-game purchase payment intents target this configured recipient. If an asset must be exchanged first, an external quote/swap provider may prepare the transaction, but the final transaction must be explicitly approved by the user's wallet and use the configured recipient. No private keys or automatic real-money execution are part of the game engine.

## Entry points

- Node.js: `cd nodejs && npm start tycoon`
- Java: `cd java && mvn package && java -cp target/classes io.amerhwitat.bizxtreme.GameLauncher tycoon`
- Python: `cd python && python -m bizxtreme tycoon`
