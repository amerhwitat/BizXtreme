using System;
using System.Threading.Tasks;

namespace BizX.Crypto
{
    [Serializable]
    public sealed class AssetBalance
    {
        public string Chain;
        public string Symbol;
        public string ContractOrMint;
        public string Address;
        public string RawAmount;
        public int Decimals;
        public long ObservedAtUnix;
        public string Source;
    }

    [Serializable]
    public sealed class TransactionRecord
    {
        public string Chain;
        public string Hash;
        public string From;
        public string To;
        public string Asset;
        public string RawAmount;
        public string Status;
        public long ObservedAtUnix;
        public string ExplorerUrl;
    }

    public interface IChainAdapter
    {
        string ChainId { get; }
        Task<AssetBalance> GetBalanceAsync(string address, string assetId = null);
        Task<TransactionRecord[]> GetTransactionsAsync(string address, int limit = 25);
        string AddressExplorer(string address);
        string TransactionExplorer(string txHash);
    }
}
