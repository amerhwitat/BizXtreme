# Health, Ammo & Checkpoints

## HUD contract
Every active gameplay screen consumes the same `hud()` state: `health/maxHealth`, `healthPercent`, `ammo/magazineSize`, `reserveAmmo`, and resource urgency state. Health and ammo are persistent gameplay counters, not screen-local values.

Recommended layout: health at the lower-left and ammo at the lower-right, with contextual low-resource warnings. This follows common combat-HUD practice where health and ammo remain immediately readable without obscuring play.

## Resource products
- Medical Kit — **$0.49 USD**, restores 40 health up to the maximum.
- Ammo Pack — **$0.29 USD**, adds 30 reserve rounds.
- Survival Bundle — **$0.69 USD**, restores 40 health and adds 60 reserve rounds.

Purchases remain explicit and are granted only after the configured purchase provider verifies the transaction.

## Depletion flow
1. Health reaches zero or both magazine and reserve ammo reach zero.
2. HUD immediately shows a purchase prompt.
3. Player may approve the low-cost item purchase.
4. If the player does not purchase or the purchase fails, the current state is checkpointed automatically.
5. The game can pause/exit safely and resume later from the saved checkpoint.
6. Checkpoint data contains resource state plus the normal game snapshot.

## Implementation
- Node.js: `nodejs/src/game/survival/index.js`
- Java: `java/src/main/java/.../game/PlayerResources.java`
- Python: `python/.../game/survival/__init__.py`
- Tycoon exposes `hud`, resource purchase, depletion, save, and resume APIs.
