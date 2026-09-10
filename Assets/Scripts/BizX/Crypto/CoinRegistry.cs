using System;
using System.Collections.Generic;

namespace BizX.Crypto
{
    [Serializable]
    public sealed class CoinDefinition
    {
        public string Symbol;
        public string Name;
        public string Family;
        public int Decimals;
        public string ExplorerAddress;
        public string ExplorerTx;
        public bool SupportsProviderSend;
    }

    public static class CoinRegistry
    {
        private static readonly CoinDefinition[] Coins =
        {
            new CoinDefinition { Symbol="BTC", Name="Bitcoin", Family="bitcoin", Decimals=8, ExplorerAddress="https://blockstream.info/address/{0}", ExplorerTx="https://blockstream.info/tx/{0}", SupportsProviderSend=false },
            new CoinDefinition { Symbol="ETH", Name="Ethereum", Family="evm", Decimals=18, ExplorerAddress="https://etherscan.io/address/{0}", ExplorerTx="https://etherscan.io/tx/{0}", SupportsProviderSend=true },
            new CoinDefinition { Symbol="BNB", Name="BNB", Family="evm", Decimals=18, ExplorerAddress="https://bscscan.com/address/{0}", ExplorerTx="https://bscscan.com/tx/{0}", SupportsProviderSend=true },
            new CoinDefinition { Symbol="MATIC", Name="Polygon", Family="evm", Decimals=18, ExplorerAddress="https://polygonscan.com/address/{0}", ExplorerTx="https://polygonscan.com/tx/{0}", SupportsProviderSend=true },
            new CoinDefinition { Symbol="AVAX", Name="Avalanche", Family="evm", Decimals=18, ExplorerAddress="https://snowtrace.io/address/{0}", ExplorerTx="https://snowtrace.io/tx/{0}", SupportsProviderSend=true },
            new CoinDefinition { Symbol="SOL", Name="Solana", Family="solana", Decimals=9, ExplorerAddress="https://solscan.io/account/{0}", ExplorerTx="https://solscan.io/tx/{0}", SupportsProviderSend=false },
            new CoinDefinition { Symbol="LTC", Name="Litecoin", Family="bitcoin-like", Decimals=8, ExplorerAddress="https://blockchair.com/litecoin/address/{0}", ExplorerTx="https://blockchair.com/litecoin/transaction/{0}", SupportsProviderSend=false },
            new CoinDefinition { Symbol="DOGE", Name="Dogecoin", Family="bitcoin-like", Decimals=8, ExplorerAddress="https://dogechain.info/address/{0}", ExplorerTx="https://dogechain.info/tx/{0}", SupportsProviderSend=false },
            new CoinDefinition { Symbol="BCH", Name="Bitcoin Cash", Family="bitcoin-like", Decimals=8, ExplorerAddress="https://blockchair.com/bitcoin-cash/address/{0}", ExplorerTx="https://blockchair.com/bitcoin-cash/transaction/{0}", SupportsProviderSend=false },
            new CoinDefinition { Symbol="XRP", Name="XRP", Family="xrp", Decimals=6, ExplorerAddress="https://xrpscan.com/account/{0}", ExplorerTx="https://xrpscan.com/tx/{0}", SupportsProviderSend=false },
            new CoinDefinition { Symbol="ADA", Name="Cardano", Family="cardano", Decimals=6, ExplorerAddress="https://cardanoscan.io/address/{0}", ExplorerTx="https://cardanoscan.io/transaction/{0}", SupportsProviderSend=false },
            new CoinDefinition { Symbol="DOT", Name="Polkadot", Family="substrate", Decimals=10, ExplorerAddress="https://polkadot.subscan.io/account/{0}", ExplorerTx="https://polkadot.subscan.io/extrinsic/{0}", SupportsProviderSend=false },
            new CoinDefinition { Symbol="TRX", Name="TRON", Family="tron", Decimals=6, ExplorerAddress="https://tronscan.org/#/address/{0}", ExplorerTx="https://tronscan.org/#/transaction/{0}", SupportsProviderSend=false },
            new CoinDefinition { Symbol="XLM", Name="Stellar", Family="stellar", Decimals=7, ExplorerAddress="https://stellar.expert/explorer/public/account/{0}", ExplorerTx="https://stellar.expert/explorer/public/tx/{0}", SupportsProviderSend=false },
            new CoinDefinition { Symbol="TON", Name="Toncoin", Family="ton", Decimals=9, ExplorerAddress="https://tonscan.org/address/{0}", ExplorerTx="https://tonscan.org/tx/{0}", SupportsProviderSend=false }
        };

        public static IReadOnlyList<CoinDefinition> All => Coins;
        public static CoinDefinition Find(string symbol) => Array.Find(Coins, c => string.Equals(c.Symbol, symbol, StringComparison.OrdinalIgnoreCase));
    }
}
