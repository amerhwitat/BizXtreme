# Game Crypto Asset Economy Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add an optional non-custodial payment and entitlement layer for free and low-price original game assets in BizXtreme.

**Architecture:** Keep gameplay and catalog ownership server-authoritative. The game client creates a server-priced payment intent; an external wallet/provider or testnet simulator settles it; the backend verifies the transaction and credits an idempotent entitlement. No private keys or player funds are held by BizXtreme.

**Tech Stack:** C++17/20, Python 3.11+, TypeScript/Node.js, JSON Schema, optional EVM/Stellar/provider adapters, testnet-first CI.

**Spec:** `docs/superpowers/specs/2026-09-13-game-crypto-asset-economy.md`

## Global Constraints

- Crypto is optional; free gameplay and free assets remain available without payment.
- Catalog prices are server-controlled and fiat-denominated; crypto is a settlement method.
- Production payment integrations are opt-in and provider/region/platform dependent.
- No custody of private keys, seed phrases or player funds.
- Development defaults to testnet/simulator mode.
- Entitlements are credited only after verified payment and idempotency checks.
- Proprietary Counter-Strike, Roblox and Minecraft assets are excluded.
- External assets require provenance and redistribution licensing.

---

### Task 1: Catalog and Payment Contract

**Files:**
- Create: `marketplace/crypto/catalog.json`
- Create: `marketplace/crypto/include/game_payment.hpp`
- Create: `marketplace/crypto/typescript/payment-gateway.ts`
- Create: `marketplace/crypto/python/payment_policy.py`
- Test: `tests/marketplace/crypto/*`

**Interfaces:**
- `validatePurchase(item, intent) -> error|null`
- `PaymentGateway::verify(intent, transaction_id)`
- `credit_only_after_verified_payment(verified, idempotency_key) -> bool`

- [ ] **Step 1: Write failing catalog and validation tests**
- [ ] **Step 2: Run the tests and verify failure**
- [ ] **Step 3: Implement server-priced catalog validation**
- [ ] **Step 4: Implement C++/Python/TypeScript contracts**
- [ ] **Step 5: Test price tampering, asset mismatch, unsupported payment method and free-item flows**
- [ ] **Step 6: Commit**

### Task 2: Testnet/Provider Payment Adapters

**Files:**
- Create: `marketplace/crypto/adapters/testnet/*`
- Create: `marketplace/crypto/adapters/provider/*`
- Create: `marketplace/crypto/README.md`
- Test: adapter unit/integration tests

**Interfaces:**
- `createPaymentIntent(order_id, asset_id)`
- `verifyPayment(transaction_id, expected_amount, expected_currency)`
- `creditEntitlement(order_id)`

- [ ] **Step 1: Write failing idempotency and verification tests**
- [ ] **Step 2: Implement deterministic testnet simulator**
- [ ] **Step 3: Implement provider adapter boundary without embedding credentials**
- [ ] **Step 4: Verify webhook/order replay protection**
- [ ] **Step 5: Commit**

### Task 3: Runtime Integration

**Files:**
- Modify: existing C++/C#/Rust/Java/Python/Node/TypeScript/Kotlin/Swift/Flutter/web marketplace adapters
- Create: runtime-specific payment facades where the runtime exists

- [ ] **Step 1: Add a common purchase request shape**
- [ ] **Step 2: Add wallet/provider handoff APIs without private-key access**
- [ ] **Step 3: Add entitlement refresh after server confirmation**
- [ ] **Step 4: Add mobile/web checkout boundaries**
- [ ] **Step 5: Commit**

### Task 4: Security, CI and Documentation

**Files:**
- Create: `docs/security/crypto-payments.md`
- Modify: `.github/workflows/*`
- Modify: `README.md`

- [ ] **Step 1: Add tests for price manipulation, replay, duplicate settlement and forged confirmations**
- [ ] **Step 2: Add testnet-only CI configuration**
- [ ] **Step 3: Document production enablement prerequisites and platform restrictions**
- [ ] **Step 4: Verify no credentials or private keys are committed**
- [ ] **Step 5: Commit**

### Task 5: Final Verification

- [ ] **Step 1: Run every available crypto/catalog test**
- [ ] **Step 2: Verify free items require no payment**
- [ ] **Step 3: Verify paid items cannot be credited without verification**
- [ ] **Step 4: Verify duplicate transaction IDs are idempotent**
- [ ] **Step 5: Verify client-controlled prices are rejected**
- [ ] **Step 6: Record unavailable blockchain/provider toolchains instead of claiming production readiness**
- [ ] **Step 7: Review changes against the crypto asset economy specification**
