from bizxtreme.monetization import MonetizationEngine, PAYMENT_ROUTING
from bizxtreme.game.survival import PlayerResources
PRIMARY_ETH_ADDRESS=PAYMENT_ROUTING["primaryEthAddress"]
PRIMARY_PAYPAL_ACCOUNT=PAYMENT_ROUTING["primaryPayPalAccount"]
BUSINESSES={"bakery":{"name":"Bakery","revenue":900,"costs":300},"market":{"name":"Market","revenue":1500,"costs":650},"factory":{"name":"Factory","revenue":2600,"costs":1200}}
class TycoonGame:
    def __init__(self,cash=0,businesses=None,monetization=None,player_resources=None): self.cash=cash; self.businesses=dict(businesses or {}); self.turn=0; self.monetization=MonetizationEngine(**(monetization or {})); self.resources=PlayerResources(**(player_resources or {}))
    def buy_business(self,business_type,price):
        if price<=0 or self.cash<price or business_type not in BUSINESSES: return {"ok":False,"reason":"invalid-purchase"}
        self.cash-=price; self.businesses[business_type]=self.businesses.get(business_type,0)+1; return {"ok":True,"business":business_type,"payment":{"asset":"ETH","recipient":PRIMARY_ETH_ADDRESS,"paypal_account":PRIMARY_PAYPAL_ACCOUNT,"amount":price,"status":"wallet-authorization-required"}}
    def purchase_pack(self,product_id,provider="store"): return self.monetization.purchase(product_id,provider)
    def request_resource_purchase(self,kind): return self.resources.request_purchase(kind)
    def apply_verified_resource_purchase(self,product_id): return self.resources.apply_verified_purchase(product_id)
    def record_ad(self,placement,provider="unityAds"): return self.monetization.record_ad_impression(placement,provider)
    def claim_rewarded_income(self,amount):
        result=self.monetization.grant_rewarded_ad("rewarded_double_income",{"cash":amount})
        if result.get("ok") and amount>0: self.cash+=amount
        return {**result,"cash":self.cash}
    def advance_turn(self):
        revenue=sum(BUSINESSES[k]["revenue"]*n for k,n in self.businesses.items()); costs=sum(BUSINESSES[k]["costs"]*n for k,n in self.businesses.items()); self.cash+=revenue-costs; self.turn+=1; return {"turn":self.turn,"revenue":revenue,"costs":costs,"profit":revenue-costs,"cash":self.cash}
    def save_checkpoint(self): return {"game":self.snapshot(),"resources":self.resources.save_checkpoint()}
    def resume_from_checkpoint(self,checkpoint): return bool(checkpoint and self.resources.resume_from_checkpoint(checkpoint.get("resources")))
    def handle_resource_depletion(self): return self.resources.handle_depletion()
    def hud(self): return {"health":self.resources.hud(),"cash":self.cash,"turn":self.turn}
    def snapshot(self): return {"turn":self.turn,"cash":self.cash,"businesses":dict(self.businesses),"resources":self.resources.hud(),"monetization":self.monetization.snapshot()}
