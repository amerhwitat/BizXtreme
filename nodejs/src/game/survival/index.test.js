import assert from 'node:assert/strict';
import { PlayerResources } from './index.js';

const p = new PlayerResources();
assert.equal(p.health, 100);
assert.equal(p.ammo, 30);
assert.equal(p.reserveAmmo, 120);
assert.equal(p.useMedicalKit(), 100);
assert.equal(p.health, 100);
assert.equal(p.addAmmo(), 150);
assert.equal(p.reserveAmmo, 150);
p.takeDamage(100);
assert.equal(p.needsPurchasePrompt().kind, 'health');
p.consumeAmmo(30);
p.useMedicalKit();
assert.equal(p.needsPurchasePrompt(), null);
for (let i = 0; i < 5; i++) {
  p.reload();
  p.consumeAmmo(30);
}
assert.equal(p.ammo, 0);
assert.equal(p.reserveAmmo, 0);
assert.equal(p.needsPurchasePrompt().kind, 'ammo');
const checkpoint = p.saveCheckpoint();
assert.equal(checkpoint.health, 40);
assert.equal(checkpoint.ammo, 0);
assert.equal(checkpoint.reserveAmmo, 0);
assert.equal(p.resumeFromCheckpoint(checkpoint), true);
console.log('survival resource tests passed');
