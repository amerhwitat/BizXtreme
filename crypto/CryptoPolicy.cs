namespace BizXtreme.Crypto;

public sealed class CryptoPolicy
{
    public bool AllowLiveNetworks { get; init; }
    public bool AllowExternalSigners { get; init; } = true;
    public bool AllowBuySell { get; init; }
    public bool AllowSwap { get; init; }
    public bool AllowSweepPlans { get; init; } = true;

    public bool Permits(IntentKind kind) => kind switch
    {
        IntentKind.Balance or IntentKind.Receive => true,
        IntentKind.Send => AllowLiveNetworks && AllowExternalSigners,
        IntentKind.Buy or IntentKind.Sell => AllowLiveNetworks && AllowBuySell,
        IntentKind.Swap or IntentKind.Exchange => AllowLiveNetworks && AllowSwap,
        IntentKind.SweepPlan => AllowSweepPlans,
        _ => false
    };
}
