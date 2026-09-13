import assert from 'node:assert/strict';
import { MonetizationEngine } from '../src/monetization/index.js';
const m = new MonetizationEngine({ testMode: true });
assert.equal(m.purchase('tycoon_premium', 'googlePlayBilling').ok, true);
assert.equal(m.snapshot().entitlements.includes('tycoon_premium'), true);
assert.equal(m.recordAdImpression('rewarded_bonus_cash', 'unityAds').ok, true);
assert.equal(m.grantRewardedAd('rewarded_bonus_cash', { cash: 100 }).ok, true);
assert.equal(m.purchase('missing', 'store').ok, false);
