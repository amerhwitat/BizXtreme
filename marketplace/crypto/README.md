# BizXtreme Game Crypto Payments

Optional, non-custodial payment abstraction for original game assets.

## Modes

- `free`: no wallet or payment required.
- `crypto_testnet`: development/testnet only.
- `crypto_mainnet_provider`: production provider boundary; disabled until configured and legally/platform reviewed.

## Purchase flow

1. Client asks the game backend for an asset purchase intent.
2. Backend loads the catalog price; client cannot set the price.
3. Client completes payment through an external wallet/provider.
4. Backend verifies the expected asset, amount, currency, destination, transaction state and idempotency key.
5. Backend grants the entitlement once.
6. Client refreshes authoritative inventory.

Do not put private keys, seed phrases or provider secrets in the client or repository.
