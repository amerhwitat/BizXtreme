RESOURCE_PRODUCTS = {
    "medical_kit": {"price": 0.49, "health": 40},
    "ammo_pack": {"price": 0.29, "reserve_ammo": 30},
    "survival_bundle": {"price": 0.69, "health": 40, "reserve_ammo": 60},
}

class PlayerResources:
    def __init__(self, max_health=100, health=None, magazine_size=30, ammo=None, reserve_ammo=120):
        self.max_health=max_health; self.health=max_health if health is None else max(0,min(max_health,health)); self.magazine_size=magazine_size; self.ammo=magazine_size if ammo is None else max(0,min(magazine_size,ammo)); self.reserve_ammo=max(0,reserve_ammo); self.checkpoint=None
    def take_damage(self, amount): self.health=max(0,self.health-max(0,amount)); return self.hud()
    def use_medical_kit(self, amount=40): self.health=min(self.max_health,self.health+amount); return self.health
    def consume_ammo(self, amount=1): used=max(0,min(self.ammo,amount)); self.ammo-=used; return used
    def add_ammo(self, amount=30): self.reserve_ammo+=max(0,amount); return self.reserve_ammo
    def reload(self): loaded=min(self.magazine_size-self.ammo,self.reserve_ammo); self.ammo+=loaded; self.reserve_ammo-=loaded; return self.hud()
    def hud(self): return {"health":self.health,"maxHealth":self.max_health,"healthPercent":self.health/self.max_health,"ammo":self.ammo,"magazineSize":self.magazine_size,"reserveAmmo":self.reserve_ammo,"ammoPercent":self.ammo/self.magazine_size}
    def needs_purchase_prompt(self):
        if self.health<=0: return {"kind":"health","productId":"medical_kit","message":"Health depleted. Purchase a medical kit or save a checkpoint to continue later."}
        if self.ammo<=0 and self.reserve_ammo<=0: return {"kind":"ammo","productId":"ammo_pack","message":"Ammo depleted. Purchase an ammo pack or save a checkpoint to continue later."}
        return None
    def request_purchase(self, kind):
        product_id = "medical_kit" if kind=="health" else "ammo_pack" if kind=="ammo" else "survival_bundle"
        return {"ok":True,"prompt":True,"productId":product_id,"price":RESOURCE_PRODUCTS[product_id]["price"],"currency":"USD","requiresExplicitUserApproval":True}
    def apply_verified_purchase(self, product_id):
        product=RESOURCE_PRODUCTS.get(product_id)
        if not product: return {"ok":False,"reason":"unknown-resource-product"}
        if product.get("health"): self.use_medical_kit(product["health"])
        if product.get("reserve_ammo"): self.add_ammo(product["reserve_ammo"])
        return {"ok":True,"productId":product_id,"hud":self.hud()}
    def save_checkpoint(self): self.checkpoint={"maxHealth":self.max_health,"health":self.health,"magazineSize":self.magazine_size,"ammo":self.ammo,"reserveAmmo":self.reserve_ammo}; return dict(self.checkpoint)
    def resume_from_checkpoint(self, checkpoint=None):
        checkpoint=checkpoint or self.checkpoint
        if not checkpoint: return False
        self.max_health=checkpoint["maxHealth"]; self.health=checkpoint["health"]; self.magazine_size=checkpoint["magazineSize"]; self.ammo=checkpoint["ammo"]; self.reserve_ammo=checkpoint["reserveAmmo"]; return True
    def handle_depletion(self):
        prompt=self.needs_purchase_prompt()
        if not prompt: return {"depleted":False,"hud":self.hud()}
        checkpoint=self.save_checkpoint(); return {"depleted":True,"prompt":prompt,"checkpoint":checkpoint,"hud":self.hud(),"canContinueLater":True}
