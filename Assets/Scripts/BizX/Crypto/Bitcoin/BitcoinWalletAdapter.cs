using System;
using System.Threading.Tasks;
using BizX.Crypto;

namespace BizX.Crypto.Bitcoin
{
    /// <summary>
    /// Bitcoin adapter boundary. Bitcoin uses UTXOs, so the production implementation
    /// must select inputs, calculate fees/change, sign locally or through a wallet provider,
    /// then broadcast and track confirmations. This interface deliberately keeps secrets
    /// outside the game and scanner layers.
    /// </summary>
    public interface IBitcoinWalletAdapter : IChainAdapter
    {
        Task<BitcoinUtxo[]> GetUtxosAsync(string address);
        Task<string> EstimateFeeRateAsync();
        Task<BitcoinPaymentPreview> PreviewPaymentAsync(string fromAddress, string toAddress, long amountSats);
        Task<BitcoinBroadcastResult> SignAndBroadcastAsync(BitcoinPaymentRequest request);
    }

    [Serializable]
    public sealed class BitcoinUtxo
    {
        public string TxId;
        public uint Vout;
        public long ValueSats;
        public int Confirmations;
    }

    [Serializable]
    public sealed class BitcoinPaymentRequest
    {
        public string FromAddress;
        public string ToAddress;
        public long AmountSats;
        public long FeeSats;
    }

    [Serializable]
    public sealed class BitcoinPaymentPreview
    {
        public string FromAddress;
        public string ToAddress;
        public long AmountSats;
        public long EstimatedFeeSats;
        public long EstimatedChangeSats;
        public bool RequiresUserApproval;
    }

    [Serializable]
    public sealed class BitcoinBroadcastResult
    {
        public bool Success;
        public string TxId;
        public string Error;
    }
}
