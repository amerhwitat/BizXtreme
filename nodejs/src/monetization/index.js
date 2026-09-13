import { readFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';

const CONFIG_PATH = fileURLToPath(new URL('../../../games/payment-config/payment-config.json', import.meta.url));
const PAYMENT_CONFIG = JSON.parse(readFileSync(CONFIG_PATH, 'utf8'));
export const PAYMENT_ROUTING = Object.freeze(PAYMENT_CONFIG.paymentRouting);

export const PRODUCTS = Object.freeze({
  starter_pack: { type: 'consumable', price: 0.99 },
  builder_pack: { type: 'consumable', price: 4.99 },
  tycoon_premium: { type: 'non_consumable', price: 9.99 },
  vip_monthly: { type: 'subscription', price: 4.99, period: 'month' },
  medical_kit: { type: 'consumable', price: 0.49 },
  ammo_pack: { type: 'consumable', price: 0.29 },
  survival_bundle: { type: 'consumable', price: 0.69 }
});
export const AD_PLACEMENTS = Object.freeze(['banner_home', 'interstitial_round_end', 'rewarded_double_income', 'rewarded_bonus_cash']);
export class MonetizationEngine {
  constructor({ testMode = true } = {}) { this.testMode = testMode; this.events = []; this.entitlements = new Set(); }
  purchase(productId, provider = 'store') {
    const product = PRODUCTS[productId];
    if (!product) return { ok: false, reason: 'unknown-product' };
    this.events.push({ type: 'purchase', productId, provider, amount: product.price, testMode: this.testMode });
    if (product.type !== 'consumable') this.entitlements.add(productId);
    return { ok: true, productId, provider, amount: product.price, status: 'verification-required', paymentMethods: { ethereum: { recipient: PAYMENT_ROUTING.primaryEthAddress, asset: 'ETH' }, paypal: { account: PAYMENT_ROUTING.primaryPayPalAccount } }, defaultPaymentMethod: PAYMENT_ROUTING.defaultMethod, fallbackPaymentMethod: PAYMENT_ROUTING.fallbackMethod, requiresExplicitUserSelection: PAYMENT_ROUTING.routingRequiresExplicitUserSelection };
  }
  recordAdImpression(placement, provider) { if (!AD_PLACEMENTS.includes(placement)) return { ok: false, reason: 'unknown-placement' }; this.events.push({ type: 'ad_impression', placement, provider, testMode: this.testMode }); return { ok: true, placement, provider }; }
  grantRewardedAd(placement, reward) { if (!placement.startsWith('rewarded_')) return { ok: false, reason: 'not-rewarded-placement' }; this.events.push({ type: 'rewarded_ad', placement, reward, testMode: this.testMode }); return { ok: true, reward }; }
  snapshot() { return { testMode: this.testMode, entitlements: [...this.entitlements], events: [...this.events] }; }
}
