package io.amerhwitat.bizxtreme.monetization;

public final class MonetizationRoutingTest {
    public static void main(String[] args) {
        MonetizationEngine engine = new MonetizationEngine(true);
        MonetizationEngine.Result result = engine.purchase("starter_pack", "game-store");
        assert result.ok();
        assert result.paymentRouting().defaultMethod().equals("ethereum");
        assert result.paymentRouting().fallbackMethod().equals("paypal");
        assert result.paymentRouting().ethereum().asset().equals("ETH");
        assert result.paymentRouting().ethereum().recipient() != null;
        assert result.paymentRouting().paypal().account() != null;
        assert result.paymentRouting().requiresExplicitUserSelection();
    }
}
