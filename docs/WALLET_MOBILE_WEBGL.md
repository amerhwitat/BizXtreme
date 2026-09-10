# BizXtreme Wallet, Mobile and WebGL Application Guide

## Purpose

BizXtreme is the extended application surface for wallet-connected WebGL and mobile experiences.

## Wallet functions

- Connect an external wallet/provider.
- Show public address, network, balances and transaction status.
- Send supported assets using provider-side signing.
- Receive assets by address or QR.
- Sign non-payment authentication challenges.
- Create encrypted local backups.
- Offer explicitly confirmed recovery-phrase/private-key export when supported by the selected wallet.

## Non-custodial security

Normal application operation never requires a recovery phrase or private key. Connected providers retain signing authority. The application sees public account information and signed transaction results, not raw signing secrets.

Recovery-phrase/private-key export is an advanced operation. It must display a prominent warning, require deliberate confirmation, save only to a user-selected local destination, and prevent telemetry, clipboard retention, server upload, or application logging of the secret. Encrypted wallet-vault backup is the recommended default.

## WebGL integration

The WebGL renderer communicates with a wallet adapter through a narrow interface:

- `connect()`
- `disconnect()`
- `getAccounts()`
- `getChain()`
- `getBalances()`
- `prepareTransaction()`
- `signTransaction()`
- `broadcastTransaction()`
- `getTransactionStatus()`
- `exportEncryptedBackup()`

Rendering code must not receive private keys. Provider adapters and secure wallet modules are responsible for signing.

## Mobile integration

The mobile application exposes the same logical wallet contract. Native secure storage may be used for encrypted local state, while external-wallet connections remain provider controlled. Device backup/export must not silently upload wallet secrets.

## Buy time

`Plan -> Quote -> Wallet Connect -> Payment Preview -> User Signature -> Confirmation -> Entitlement`

Entitlements should be tied to a transaction/order reference and validated independently from the signing secret.

## Accessories

`Catalog -> Product -> Cart -> Quote -> Wallet Payment -> Confirmation -> Fulfillment`

Orders contain public wallet address, product/order metadata and transaction references only. Never request a seed phrase or private key for an order.

## Transaction UX

Before a payment, show:

- network;
- recipient/contract;
- asset;
- amount;
- estimated network fee;
- total;
- order or entitlement reference.

The user must explicitly approve the transaction in the wallet. Failed, rejected, replaced and pending transactions receive separate UI states.

## Documentation references

Ethereum's wallet documentation describes wallets as interfaces for managing accounts, sending transactions, receiving funds and connecting to applications. Recovery phrases/private keys remain the user's responsibility. This project follows that non-custodial model.
