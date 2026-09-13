package io.amerhwitat.bizxtreme.game;

import java.util.Map;

public final class PlayerResources {
    public record PurchasePrompt(String kind, String productId, double price, String message) {}
    public record Checkpoint(int maxHealth, int health, int magazineSize, int ammo, int reserveAmmo) {}
    private int maxHealth = 100, health = 100, magazineSize = 30, ammo = 30, reserveAmmo = 120;
    private Checkpoint checkpoint;
    public int health() { return health; }
    public int maxHealth() { return maxHealth; }
    public int ammo() { return ammo; }
    public int reserveAmmo() { return reserveAmmo; }
    public Map<String,Number> hud() { return Map.of("health", health, "maxHealth", maxHealth, "healthPercent", (double) health / maxHealth, "ammo", ammo, "magazineSize", magazineSize, "reserveAmmo", reserveAmmo, "ammoPercent", (double) ammo / magazineSize); }
    public void takeDamage(int amount) { health = Math.max(0, health - Math.max(0, amount)); }
    public void useMedicalKit() { health = Math.min(maxHealth, health + 40); }
    public void consumeAmmo(int amount) { ammo = Math.max(0, ammo - Math.max(0, amount)); }
    public void addAmmo() { reserveAmmo += 30; }
    public void reload() { int loaded = Math.min(magazineSize - ammo, reserveAmmo); ammo += loaded; reserveAmmo -= loaded; }
    public PurchasePrompt purchasePrompt() {
        if (health <= 0) return new PurchasePrompt("health", "medical_kit", 0.49, "Health depleted. Purchase a medical kit or save a checkpoint to continue later.");
        if (ammo <= 0 && reserveAmmo <= 0) return new PurchasePrompt("ammo", "ammo_pack", 0.29, "Ammo depleted. Purchase an ammo pack or save a checkpoint to continue later.");
        return null;
    }
    public PurchasePrompt requestPurchase(String kind) { return "health".equals(kind) ? new PurchasePrompt("health", "medical_kit", 0.49, "Purchase a medical kit?") : new PurchasePrompt("ammo", "ammo_pack", 0.29, "Purchase an ammo pack?"); }
    public boolean applyVerifiedPurchase(String productId) { switch (productId) { case "medical_kit" -> useMedicalKit(); case "ammo_pack" -> addAmmo(); default -> { return false; } } return true; }
    public Checkpoint saveCheckpoint() { checkpoint = new Checkpoint(maxHealth, health, magazineSize, ammo, reserveAmmo); return checkpoint; }
    public boolean resumeFromCheckpoint(Checkpoint value) { if (value == null) return false; maxHealth=value.maxHealth(); health=value.health(); magazineSize=value.magazineSize(); ammo=value.ammo(); reserveAmmo=value.reserveAmmo(); return true; }
    public Checkpoint checkpoint() { return checkpoint; }
}
