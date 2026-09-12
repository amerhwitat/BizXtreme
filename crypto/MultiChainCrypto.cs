using System;
using System.Collections.Generic;

namespace BizXtreme.Crypto;

public enum NetworkKind { Utxo, Evm, Solana, Ton, Other }
public enum IntentKind { Balance, Receive, Send, Buy, Sell, Swap, Exchange, SweepPlan }

public sealed record CoinDescriptor(
    string ChainId,
    string AssetId,
    string Symbol,
    string Name,
    uint Decimals,
    NetworkKind Network,
    bool SupportsSend = false,
    bool SupportsReceive = true,
    bool SupportsSwap = false);

public sealed record WalletAccount(string ChainId, string Address, bool WatchOnly = true);
public sealed record Balance(CoinDescriptor Coin, string RawAmount, string DisplayAmount, string FiatValue);

public sealed record TransactionIntent(
    IntentKind Kind,
    string ChainId,
    string AssetId,
    string From,
    string To,
    string Amount,
    string Memo = "",
    string QuoteId = "",
    bool RequiresUserConfirmation = true);

public interface IChainAdapter
{
    string ChainId { get; }
    IReadOnlyList<Balance> GetBalances(WalletAccount account);
    string GetReceiveAddress(WalletAccount account);
    TransactionIntent BuildSend(WalletAccount account, string assetId, string to, string amount);
}

public interface ICryptoGateway
{
    IReadOnlyList<CoinDescriptor> DiscoverAssets();
    IReadOnlyList<Balance> ScanBalances(WalletAccount account);
    TransactionIntent QuoteSwap(string sourceAsset, string targetAsset, string amount);
    TransactionIntent BuildSweepPlan(WalletAccount account);
}
