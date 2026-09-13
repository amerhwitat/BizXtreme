from bizxtreme.game.survival import PlayerResources

p = PlayerResources(); assert p.health == 100; assert p.ammo == 30; assert p.reserve_ammo == 120
p.take_damage(100); assert p.needs_purchase_prompt()["kind"] == "health"
checkpoint = p.save_checkpoint(); assert checkpoint["health"] == 0; assert p.resume_from_checkpoint(checkpoint) is True

a = PlayerResources(reserve_ammo=0); a.consume_ammo(30); assert a.needs_purchase_prompt()["kind"] == "ammo"
ammo_checkpoint = a.save_checkpoint(); assert ammo_checkpoint["ammo"] == 0; assert a.resume_from_checkpoint(ammo_checkpoint) is True
assert a.request_purchase("health")["price"] == 0.49
assert a.request_purchase("ammo")["price"] == 0.29
print("survival resource tests passed")
