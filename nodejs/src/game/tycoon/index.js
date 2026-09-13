import { MonetizationEngine, PAYMENT_ROUTING } from '../../monetization/index.js';
import { PlayerResources } from '../survival/index.js';
const PRIMARY_ETH_ADDRESS = PAYMENT_ROUTING.primaryEthAddress;
const PRIMARY_PAYPAL_ACCOUNT = PAYMENT_ROUTING.primaryPayPalAccount;
const DEFAULT_BUSINESSES = Object.freeze({ bakery: { name: 'Bakery', revenue: 900, costs: 300 }, market: { name: 'Market', revenue: 1500, costs: 650 }, factory: { name: 'Factory', revenue: 2600, costs: 1200 } });
export class TycoonGame {
  constructor({ cash = 0, businesses = {}, monetization = {}, playerResources = {} } = {}) { this.cash = cash; this.businesses = { ...businesses }; this.turn = 0; this.monetization = new MonetizationEngine(monetization); this.resources = new PlayerResources(playerResources); }
  buyBusiness(type, price) { if (!Number.isFinite(price) || price <= 0 || this.cash < price) return { ok: false, reason: 'insufficient-funds-or-invalid-price' }; if (!DEFAULT_BUSINESSES[type]) return { ok: false, reason: 'unknown-business' }; this.cash -= price; this.businesses[type] = (this.businesses[type] ?? 0) + 1; return { ok: true, business: type, payment: { asset: 'ETH', recipient: PRIMARY_ETH_ADDRESS, paypalAccount: PRIMARY_PAYPAL_ACCOUNT, amount: price, status: 'wallet-authorization-required' } }; }
  purchasePack(productId, provider = 'store') { return this.monetization.purchase(productId, provider); }
  requestResourcePurchase(kind) { return this.resources.requestPurchase(kind); }
  applyVerifiedResourcePurchase(productId) { return this.resources.applyVerifiedPurchase(productId); }
  recordAd(placement, provider = 'unityAds') { return this.monetization.recordAdImpression(placement, provider); }
  claimRewardedIncome(amount) { const result = this.monetization.grantRewardedAd('rewarded_double_income', { cash: amount }); if (result.ok && Number.isFinite(amount) && amount > 0) this.cash += amount; return { ...result, cash: this.cash }; }
  advanceTurn() { let revenue = 0, costs = 0; for (const [type, count] of Object.entries(this.businesses)) { const d = DEFAULT_BUSINESSES[type]; revenue += d.revenue * count; costs += d.costs * count; } this.cash += revenue - costs; this.turn += 1; return { turn: this.turn, revenue, costs, profit: revenue - costs, cash: this.cash }; }
  handleResourceDepletion() { return this.resources.handleDepletion(); }
  saveCheckpoint() { return { game: this.snapshot(), resources: this.resources.saveCheckpoint() }; }
  resumeFromCheckpoint(checkpoint) { return Boolean(checkpoint?.resources) && this.resources.resumeFromCheckpoint(checkpoint.resources); }
  hud() { return { health: this.resources.hud(), cash: this.cash, turn: this.turn }; }
  snapshot() { return { turn: this.turn, cash: this.cash, businesses: { ...this.businesses }, resources: this.resources.hud(), monetization: this.monetization.snapshot() }; }
}
export { PRIMARY_ETH_ADDRESS, PRIMARY_PAYPAL_ACCOUNT, DEFAULT_BUSINESSES };
