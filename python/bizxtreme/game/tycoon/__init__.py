PRIMARY_ETH_ADDRESS = "0x0B4fF3fc6AE19fAF9A0d2628a646ABD9636B1162"
BUSINESSES = {"bakery": {"name": "Bakery", "revenue": 900, "costs": 300}, "market": {"name": "Market", "revenue": 1500, "costs": 650}, "factory": {"name": "Factory", "revenue": 2600, "costs": 1200}}

class TycoonGame:
    def __init__(self, cash=0, businesses=None): self.cash=cash; self.businesses=dict(businesses or {}); self.turn=0
    def buy_business(self, business_type, price):
        if price <= 0 or self.cash < price or business_type not in BUSINESSES: return {"ok": False, "reason": "invalid-purchase"}
        self.cash -= price; self.businesses[business_type] = self.businesses.get(business_type, 0) + 1
        return {"ok": True, "business": business_type, "payment": {"asset":"ETH", "recipient":PRIMARY_ETH_ADDRESS, "amount":price, "status":"wallet-authorization-required"}}
    def advance_turn(self):
        revenue=sum(BUSINESSES[k]["revenue"]*n for k,n in self.businesses.items()); costs=sum(BUSINESSES[k]["costs"]*n for k,n in self.businesses.items())
        self.cash += revenue-costs; self.turn += 1
        return {"turn":self.turn,"revenue":revenue,"costs":costs,"profit":revenue-costs,"cash":self.cash}
    def snapshot(self): return {"turn":self.turn,"cash":self.cash,"businesses":dict(self.businesses)}
