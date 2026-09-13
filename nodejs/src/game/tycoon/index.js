const PRIMARY_ETH_ADDRESS = '0x0B4fF3fc6AE19fAF9A0d2628a646ABD9636B1162';

const DEFAULT_BUSINESSES = Object.freeze({
  bakery: { name: 'Bakery', revenue: 900, costs: 300 },
  market: { name: 'Market', revenue: 1500, costs: 650 },
  factory: { name: 'Factory', revenue: 2600, costs: 1200 }
});

export class TycoonGame {
  constructor({ cash = 0, businesses = {} } = {}) { this.cash = cash; this.businesses = { ...businesses }; this.turn = 0; }
  buyBusiness(type, price) {
    if (!Number.isFinite(price) || price <= 0 || this.cash < price) return { ok: false, reason: 'insufficient-funds-or-invalid-price' };
    if (!DEFAULT_BUSINESSES[type]) return { ok: false, reason: 'unknown-business' };
    this.cash -= price;
    this.businesses[type] = (this.businesses[type] ?? 0) + 1;
    return { ok: true, business: type, payment: { asset: 'ETH', recipient: PRIMARY_ETH_ADDRESS, amount: price, status: 'wallet-authorization-required' } };
  }
  advanceTurn() {
    let revenue = 0, costs = 0;
    for (const [type, count] of Object.entries(this.businesses)) { revenue += DEFAULT_BUSINESSES[type].revenue * count; costs += DEFAULT_BUSINESSES[type].costs * count; }
    this.cash += revenue - costs; this.turn += 1;
    return { turn: this.turn, revenue, costs, profit: revenue - costs, cash: this.cash };
  }
  snapshot() { return { turn: this.turn, cash: this.cash, businesses: { ...this.businesses } }; }
}
export { PRIMARY_ETH_ADDRESS, DEFAULT_BUSINESSES };
