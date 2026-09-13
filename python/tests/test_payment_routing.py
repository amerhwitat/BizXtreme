from bizxtreme.monetization import MonetizationEngine


def test_purchase_exposes_configured_payment_routing():
    result = MonetizationEngine(test_mode=True).purchase("starter_pack", "game-store")
    assert result["ok"] is True
    assert result["payment_methods"]["ethereum"]["asset"] == "ETH"
    assert result["payment_methods"]["ethereum"]["recipient"]
    assert result["payment_methods"]["paypal"]["account"]
    assert result["default_payment_method"] == "ethereum"
    assert result["fallback_payment_method"] == "paypal"
    assert result["requires_explicit_user_selection"] is True
