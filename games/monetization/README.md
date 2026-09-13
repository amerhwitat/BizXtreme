# Game Monetization

BizXtreme uses a provider-neutral monetization layer so the same game economy can target mobile stores, ad mediation, subscriptions, and optional web checkout without embedding secrets.

## Supported adapters

- Unity Ads / Unity LevelPlay
- AppLovin MAX
- Google AdMob / Google Ad Manager
- Google Play Billing for Android digital goods
- Apple StoreKit / App Store Connect for Apple digital goods
- RevenueCat for subscription and entitlement orchestration

Unity documents direct Ads SDK integration and LevelPlay mediation; Unity Ads can also participate in AppLovin, Google, and LevelPlay bidding. Google Play Billing supports one-time digital purchases and subscriptions. Apple StoreKit provides the current in-app purchase APIs. RevenueCat can track ad revenue and rewarded-ad entitlements when configured with supported ad networks.

## Game monetization logic

The adapter-neutral engine supports:

1. Consumable purchases
2. Non-consumable premium unlocks
3. Monthly subscriptions
4. Banner/interstitial/rewarded ad placements
5. Rewarded-ad grants
6. Revenue and purchase event accounting
7. Server-side purchase verification hooks
8. Test/sandbox mode
9. Provider configuration without secrets in Git

The Tycoon game uses this layer for premium packs, VIP access, rewarded income, and purchase/revenue events.

## Production setup

Create the application/product IDs in each provider dashboard and inject IDs/secrets through the deployment environment. Never commit API keys, store credentials, wallet private keys, recovery phrases, or signing secrets.

The existing ETH payment configuration remains non-custodial: real transfers/swaps require explicit wallet authorization.
