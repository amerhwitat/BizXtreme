export const PRODUCTS = Object.freeze({
  starter_pack: { type: 'consumable', price: 0.99 },
  builder_pack: { type: 'consumable', price: 4.99 },
  tycoon_premium: { type: 'non_consumable', price: 9.99 },
  vip_monthly: { type: 'subscription', price: 4.99, period: 'month' }
});
export const AD_PLACEMENTS = Object.freeze(['banner_home', 'interstitial_round_end', 'rewarded_double_income', 'rewarded_bonus_cash']);
export class MonetizationEngine {
  constructor({ testMode = true } = {}) { this.testMode = testMode; this.events = []; this.entitlements = new Set(); }
  purchase(productId, provider = 'store') {
    const product = PRODUCTS[productId];
    if (!product) return { ok: false, reason: 'unknown-product' };
    this.events.push({ type: 'purchase', productId, provider, amount: product.price, testMode: this.testMode });
    if (product.type !== 'consumable') this.entitlements.add(productId);
    return { ok: true, productId, provider, amount: product.price, status: 'verification-required' };
  }
  recordAdImpression(placement, provider) {
    if (!AD_PLACEMENTS.includes(placement)) return { ok: false, reason: 'unknown-placement' };
    this.events.push({ type: 'ad_impression', placement, provider, testMode: this.testMode });
    return { ok: true, placement, provider };
  }
  grantRewardedAd(placement, reward) {
    if (!placement.startsWith('rewarded_')) return { ok: false, reason: 'not-rewarded-placement' };
    this.events.push({ type: 'rewarded_ad', placement, reward, testMode: this.testMode });
    return { ok: true, reward };
  }
  snapshot() { return { testMode: this.testMode, entitlements: [...this.entitlements], events: [...this.events] }; }
}
