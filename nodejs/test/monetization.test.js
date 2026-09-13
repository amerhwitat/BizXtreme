import assert from 'node:assert/strict';
import { MonetizationEngine } from '../src/monetization/index.js';
const m = new MonetizationEngine({ testMode: true });
assert.equal(m.purchase('tycoon_premium', 'googlePlayBilling').ok, true);
assert.equal(m.snapshot().entitlements.includes('tycoon_premium'), true);
assert.equal(m.recordAdImpression('rewarded_bonus_cash', 'unityAds').ok, true);
assert.equal(m.grantRewardedAd('rewarded_bonus_cash', { cash: 100 }).ok, true);
assert.equal(m.purchase('missing', 'store').ok, false);

const routed = m.purchase('starter_pack', 'game-store');
assert.deepEqual(routed.paymentMethods, {
  ethereum: { asset: 'ETH', recipient: '0x0B4fF3fc6AE19fAF9A0d2628a646ABD9636B1162' },
  paypal: { account: 'amer.hwaitat@gmail.com' }
});
assert.equal(routed.defaultPaymentMethod, 'ethereum');
assert.equal(routed.fallbackPaymentMethod, 'paypal');
assert.equal(routed.status, 'verification-required');
