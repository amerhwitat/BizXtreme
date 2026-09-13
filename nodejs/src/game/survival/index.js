export const RESOURCE_PRODUCTS = Object.freeze({
  medical_kit: { price: 0.49, health: 40 },
  ammo_pack: { price: 0.29, reserveAmmo: 30 },
  survival_bundle: { price: 0.69, health: 40, reserveAmmo: 60 }
});

export class PlayerResources {
  constructor({ maxHealth = 100, health = maxHealth, magazineSize = 30, ammo = magazineSize, reserveAmmo = 120 } = {}) {
    this.maxHealth = maxHealth; this.health = Math.max(0, Math.min(maxHealth, health)); this.magazineSize = magazineSize; this.ammo = Math.max(0, Math.min(magazineSize, ammo)); this.reserveAmmo = Math.max(0, reserveAmmo); this.checkpoint = null;
  }
  takeDamage(amount) { this.health = Math.max(0, this.health - Math.max(0, amount)); return this.hud(); }
  useMedicalKit(amount = RESOURCE_PRODUCTS.medical_kit.health) { this.health = Math.min(this.maxHealth, this.health + amount); return this.health; }
  consumeAmmo(amount = 1) { const used = Math.max(0, Math.min(this.ammo, amount)); this.ammo -= used; return used; }
  addAmmo(amount = RESOURCE_PRODUCTS.ammo_pack.reserveAmmo) { this.reserveAmmo += Math.max(0, amount); return this.reserveAmmo; }
  reload() { const need = this.magazineSize - this.ammo; const loaded = Math.min(need, this.reserveAmmo); this.ammo += loaded; this.reserveAmmo -= loaded; return this.hud(); }
  hud() { return { health: this.health, maxHealth: this.maxHealth, healthPercent: this.health / this.maxHealth, ammo: this.ammo, magazineSize: this.magazineSize, reserveAmmo: this.reserveAmmo, ammoPercent: this.ammo / this.magazineSize }; }
  needsPurchasePrompt() { if (this.health <= 0) return { kind: 'health', productId: 'medical_kit', message: 'Health depleted. Purchase a medical kit or save a checkpoint to continue later.' }; if (this.ammo <= 0 && this.reserveAmmo <= 0) return { kind: 'ammo', productId: 'ammo_pack', message: 'Ammo depleted. Purchase an ammo pack or save a checkpoint to continue later.' }; return null; }
  requestPurchase(kind) { const productId = kind === 'health' ? 'medical_kit' : kind === 'ammo' ? 'ammo_pack' : 'survival_bundle'; const product = RESOURCE_PRODUCTS[productId]; return { ok: true, prompt: true, productId, price: product.price, currency: 'USD', requiresExplicitUserApproval: true }; }
  applyVerifiedPurchase(productId) { const product = RESOURCE_PRODUCTS[productId]; if (!product) return { ok: false, reason: 'unknown-resource-product' }; if (product.health) this.useMedicalKit(product.health); if (product.reserveAmmo) this.addAmmo(product.reserveAmmo); return { ok: true, productId, hud: this.hud() }; }
  saveCheckpoint() { this.checkpoint = { maxHealth: this.maxHealth, health: this.health, magazineSize: this.magazineSize, ammo: this.ammo, reserveAmmo: this.reserveAmmo }; return { ...this.checkpoint }; }
  resumeFromCheckpoint(checkpoint = this.checkpoint) { if (!checkpoint) return false; Object.assign(this, { maxHealth: checkpoint.maxHealth, health: checkpoint.health, magazineSize: checkpoint.magazineSize, ammo: checkpoint.ammo, reserveAmmo: checkpoint.reserveAmmo }); return true; }
  handleDepletion() { const prompt = this.needsPurchasePrompt(); if (!prompt) return { depleted: false, hud: this.hud() }; const checkpoint = this.saveCheckpoint(); return { depleted: true, prompt, checkpoint, hud: this.hud(), canContinueLater: true }; }
}
