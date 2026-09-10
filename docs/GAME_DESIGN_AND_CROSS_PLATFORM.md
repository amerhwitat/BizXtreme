# BizXtreme Game Design and Cross-Platform Architecture

## Original game preserved

The core gameplay remains the center of BizXtreme. Wallets, marketplace features and blockchain explorers are supporting systems, not replacements for gameplay.

## Main menu

The professional launcher/dashboard exposes:

- Play / Continue
- Missions
- Events
- Inventory
- Marketplace
- Wallet
- Receive / Send
- Wallet backup
- Settings

## New story content

The first campaign expansion is **The Living Frontier** with Awakening, The Broken Signal, Frontier Alliance, The Black Aurora and The Great Expedition chapters. The data-driven story format allows future chapters without changing the core client architecture.

## Live events

Weekly Frontier Weekend, seasonal Aurora Night, monthly Faction Wars, rotating Lost Signal Hunt and the Great Expedition provide replayable activities. Purchases may accelerate progression but core gameplay remains accessible without purchases.

## Free starter experience

Every new player can receive a one-time Frontier Starter Pack containing an outfit, explorer tool, vehicle skin, map, supply crates and inventory expansion. Granting is idempotent so reconnecting cannot duplicate rewards.

## Marketplace

The marketplace now includes time access, XP boosts, inventory expansion, cosmetics, map content, seasonal cosmetics, expedition equipment, resource caches and physical accessories. Purchases use preview -> user approval/signing -> broadcast -> independent confirmation -> entitlement/fulfillment.

## Wallet architecture

Wallet secrets must remain inside the wallet boundary or protected platform storage. The game and scanners consume public addresses, balances and transaction states. Seed/private-key backup must be explicit, user-controlled and never transmitted to game servers.

## Bitcoin

BTC is a first-class adapter target. The adapter models UTXOs, fee estimation, payment preview, signing/broadcast and confirmation. Bitcoin transaction construction must respect the UTXO model and change/fee rules. citeturn0search1turn0search7

## Cross-platform

The Unity architecture is organized around platform-neutral C# interfaces with platform-specific wallet/provider bridges. Target profiles include Windows, macOS, Linux, Android, iOS and WebGL. Unity documents these target families and notes that platform-specific hardware/deployment differences can require targeted implementation. citeturn0search4turn0search17

Input should use Unity's extensible Input System so keyboard/mouse, gamepad and touch controls can share the same gameplay actions. citeturn0search9

## Production status

This repository contains source-level architecture and integration layers. A packaged APK/WebGL binary is not considered reverse-engineered merely because an integration layer exists. Final production builds still require the actual Unity project, platform SDK configuration, signing credentials and CI/build verification.
