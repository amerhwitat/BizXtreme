import json
from pathlib import Path

_CONFIG_PATH = Path(__file__).resolve().parents[3] / "games" / "payment-config" / "payment-config.json"
_PAYMENT_CONFIG = json.loads(_CONFIG_PATH.read_text(encoding="utf-8"))
PAYMENT_ROUTING = _PAYMENT_CONFIG["paymentRouting"]

PRODUCTS = {
    "starter_pack": {"type": "consumable", "price": 0.99},
    "builder_pack": {"type": "consumable", "price": 4.99},
    "tycoon_premium": {"type": "non_consumable", "price": 9.99},
    "vip_monthly": {"type": "subscription", "price": 4.99, "period": "month"},
}
AD_PLACEMENTS = {"banner_home", "interstitial_round_end", "rewarded_double_income", "rewarded_bonus_cash"}

class MonetizationEngine:
    def __init__(self, test_mode=True):
        self.test_mode = test_mode
        self.events = []
        self.entitlements = set()

    def purchase(self, product_id, provider="store"):
        product = PRODUCTS.get(product_id)
        if not product:
            return {"ok": False, "reason": "unknown-product"}
        self.events.append({"type": "purchase", "product_id": product_id, "provider": provider, "amount": product["price"], "test_mode": self.test_mode})
        if product["type"] != "consumable":
            self.entitlements.add(product_id)
        routing = PAYMENT_ROUTING
        return {
            "ok": True,
            "product_id": product_id,
            "provider": provider,
            "amount": product["price"],
            "status": "verification-required",
            "payment_methods": {
                "ethereum": {"asset": "ETH", "recipient": routing["primaryEthAddress"]},
                "paypal": {"account": routing["primaryPayPalAccount"]},
            },
            "default_payment_method": routing["defaultMethod"],
            "fallback_payment_method": routing["fallbackMethod"],
            "requires_explicit_user_selection": routing["routingRequiresExplicitUserSelection"],
        }

    def record_ad_impression(self, placement, provider):
        if placement not in AD_PLACEMENTS:
            return {"ok": False, "reason": "unknown-placement"}
        self.events.append({"type": "ad_impression", "placement": placement, "provider": provider, "test_mode": self.test_mode})
        return {"ok": True, "placement": placement, "provider": provider}

    def grant_rewarded_ad(self, placement, reward):
        if not placement.startswith("rewarded_"):
            return {"ok": False, "reason": "not-rewarded-placement"}
        self.events.append({"type": "rewarded_ad", "placement": placement, "reward": reward, "test_mode": self.test_mode})
        return {"ok": True, "reward": reward}

    def snapshot(self):
        return {"test_mode": self.test_mode, "entitlements": sorted(self.entitlements), "events": list(self.events)}
