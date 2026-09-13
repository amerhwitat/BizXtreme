import test from 'node:test';
import assert from 'node:assert/strict';
import { TycoonGame } from '../src/game/tycoon/index.js';

test('Tycoon purchase routes payment to the configured primary ETH address', () => {
  const game = new TycoonGame({ cash: 10000 });
  const result = game.buyBusiness('bakery', 2500);
  assert.equal(result.ok, true);
  assert.equal(result.payment.recipient, '0x0B4fF3fc6AE19fAF9A0d2628a646ABD9636B1162');
  assert.equal(game.cash, 7500);
});

test('Tycoon turn produces revenue and applies operating costs', () => {
  const game = new TycoonGame({ cash: 10000 });
  game.buyBusiness('bakery', 2500);
  const before = game.cash;
  const result = game.advanceTurn();
  assert.ok(result.revenue > 0);
  assert.ok(result.costs > 0);
  assert.equal(game.cash, before + result.revenue - result.costs);
});
