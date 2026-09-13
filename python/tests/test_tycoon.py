from bizxtreme.game.tycoon import TycoonGame


def test_purchase_uses_configured_payment_routes():
    game = TycoonGame(cash=10_000)
    result = game.buy_business("bakery", 2_500)
    assert result["ok"] is True
    assert result["payment"]["recipient"] == "0x0B4fF3fc6AE19fAF9A0d2628a646ABD9636B1162"
    assert result["payment"]["paypal_account"] == "amer.hwaitat@gmail.com"
    assert game.cash == 7_500


def test_turn_produces_revenue_and_costs():
    game = TycoonGame(cash=10_000)
    game.buy_business("bakery", 2_500)
    before = game.cash
    result = game.advance_turn()
    assert result["revenue"] > 0
    assert result["costs"] > 0
    assert game.cash == before + result["revenue"] - result["costs"]
