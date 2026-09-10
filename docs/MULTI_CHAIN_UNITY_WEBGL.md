# BizXtreme Multi-Chain, Unity and WebGL Implementation

## Application audit

The repository currently contains a packaged Android APK and a packaged WebGL build alongside integration JSON and documentation. The repository contents do not expose the original Unity project source. Therefore this change adds a source-level integration layer rather than claiming that the packaged binaries were decompiled or modified in place.

## Wallet adapter

`Assets/Scripts/BizX/Crypto/EvmWalletClient.cs` is the Unity-facing API. `Assets/Plugins/WebGL/BizXWallet.jslib` bridges Unity to the browser's EVM provider (`window.ethereum`). Unity documents `.jslib` browser plugins and C# calls through `DllImport("__Internal")` for WebGL integrations. citeturn0search3turn0search7

Supported operations in the reference adapter:

- request wallet connection;
- read native EVM balance;
- request provider-side native transaction signing/broadcast;
- return transaction hash/error to Unity.

Production adapters should add chain-ID validation, checksum/address validation, gas estimation, transaction simulation, nonce handling and explicit payment previews before signing.

## Chain coverage

The registry covers reference adapters for BTC, ETH/EVM, BNB, Polygon, Avalanche, SOL/SPL, LTC, DOGE, BCH, XRP, ADA, DOT, TRX, XLM and TON. It is an extensible registry, not a claim that every cryptocurrency or token in existence has been hard-coded.

Ethereum reads use JSON-RPC concepts; Solana token balances follow Solana's structured RPC model. citeturn0search8turn0search4

## Explorers and scanners

Each chain has address and transaction explorer templates. A scanner layer should normalize public chain/indexer responses into:

`AssetBalance`, `TransactionRecord`, `TokenHolding`, `ConfirmationState`, `ExplorerReference`.

Scanners never receive signing secrets.

## Game economy

The catalog supports time access, XP boosts, inventory slots, cosmetic items, explorer/map content, and physical accessories. Payment is separated from entitlement/fulfillment so a confirmed transaction cannot directly execute arbitrary game code.

## Mobile architecture

Android/native builds should implement the same `IWalletProvider` contract using the platform's approved wallet/deep-link APIs or an audited wallet SDK. Secrets stay inside the wallet boundary or OS-protected secure storage. A generic mobile adapter must not assume that one wallet protocol works for every chain.

## Reverse engineering

For the existing APK/WebGL binaries, source-level reverse engineering is not claimed by these commits. A true binary audit requires the actual binary bytes and should produce an artifact manifest, package/component inventory, permissions/API inventory and reproducible findings. The newly added source tree is an auditable replacement/integration layer.
