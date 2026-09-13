# Game Crypto Asset Economy

## Goal

Add an optional, non-custodial crypto payment layer for BizXtreme games that supports free content and low-price digital asset purchases without making cryptocurrency required for gameplay.

## Principles

- Free gameplay and a free asset catalog remain available without cryptocurrency.
- Paid assets use fixed fiat-denominated catalog prices; crypto is only a settlement method.
- No proprietary Counter-Strike, Roblox or Minecraft assets are sold or redistributed.
- The game backend is authoritative for entitlement and inventory state.
- Wallets are external/self-custodial or delegated to a separately licensed payment provider; BizXtreme does not hold private keys or player funds.
- Never require players to expose seed phrases or private keys.
- Purchases are idempotent and credited only after verified payment confirmation.
- Sandbox/testnet mode is the default for development.
- Regional availability, age restrictions, taxes, consumer protection and platform-store rules must be checked before production payments are enabled.
- The system supports administrative entitlement reversal/refund workflows even though blockchain transfers themselves are not reversible.

## Catalog model

Each item contains `asset_id`, `free`, `fiat_price_minor`, `currency`, `accepted_payment_methods`, `license`, and `entitlement_policy`.

Recommended starter tiers:

- Free: 0.00
- Starter: 0.49
- Standard: 0.99
- Premium: 2.99
- Creator Pack: 4.99

Prices are configuration examples, not financial advice or a guarantee of affordability.

## Payment abstraction

```text
Game Client -> Game Backend -> Payment Adapter -> External Wallet/Provider
                      |
                      +-> Payment Verification -> Entitlement Ledger -> Inventory
```

Supported adapter categories:

- generic EVM-compatible payment adapter
- stablecoin adapter
- Stellar payment adapter
- provider/SDK adapter
- testnet simulator

The core game never depends on one chain or vendor.

## Security

- Server-side price lookup; clients cannot set price.
- Server-side asset entitlement checks.
- Signed webhook verification.
- Replay/idempotency protection using order IDs and transaction IDs.
- Confirmations/finality policy configurable per chain.
- Per-account spending limits and optional parental/admin controls.
- Fraud/risk state separate from gameplay state.
- No private-key storage in game clients.
- No speculative token issuance is required.

## Asset licensing

Every paid or free external asset requires provenance metadata: source, author, license, license URL, acquisition date, SHA-256, modifications and redistribution status. Original/generated assets are preferred.

## Runtime adapters

The contract is exposed to C++, Unreal C++, C#, Rust, Java, Python, Node.js/TypeScript, Kotlin, Swift, Dart/Flutter and web clients through runtime-specific adapters. Payment verification remains server-side.

## References

Current ecosystem research indicates that game marketplaces commonly use stablecoin settlement and server-side crediting, while wallet SDKs can provide embedded game payment flows. These patterns inform the abstraction but are not dependencies of the BizXtreme implementation.
