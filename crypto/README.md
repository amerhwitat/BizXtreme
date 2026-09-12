# BizXtreme Multi-Chain Crypto

BizXtreme exposes a Unity/game-safe crypto boundary for wallet discovery, balance scanning, receive addresses, transaction intents, buy/sell provider adapters, swaps/exchanges and sweep planning.

The architecture is deliberately not limited to a fixed list of coins. `IChainAdapter` allows native assets and token standards to be added independently of Unity scenes and game code.

## Supported families

- Bitcoin/UTXO
- EVM chains and token standards
- Solana/SPL
- TON
- additional networks through adapters

## Security

Private keys, seed phrases and signing secrets never enter Unity assets, ScriptableObjects, game saves, telemetry or logs. The default runtime is watch-only/read-only. Live send/buy/sell/swap/sweep flows create explicit intents and hand signing to a user-controlled wallet/provider.

Sweep means "discover balances and prepare a plan" until each transaction is explicitly approved. Unknown tokens are read-only until metadata and policy checks pass.

## Open-source research

Architecture is informed by public work such as Tether WDK, Wallet Standard, WalletConnect specifications and Uniswap Smart Order Router. BizXtreme does not vendor or copy their implementation; adapters preserve third-party licenses.

- https://wdk.tether.io/
- https://github.com/wallet-standard/wallet-standard
- https://github.com/WalletConnect/walletconnect-specs
- https://github.com/Uniswap/smart-order-router
