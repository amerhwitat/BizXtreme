from . import PlayerResources

p = PlayerResources()
assert p.health == 100
assert p.ammo == 30
assert p.reserve_ammo == 120
p.take_damage(100)
assert p.purchase_prompt()["kind"] == "health"
p.consume_ammo(30)
assert p.purchase_prompt()["kind"] == "ammo"
checkpoint = p.save_checkpoint()
assert checkpoint["health"] == 0
assert checkpoint["ammo"] == 0
assert p.resume_from_checkpoint(checkpoint) is True
print("survival resource tests passed")
