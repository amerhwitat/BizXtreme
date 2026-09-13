import test from 'node:test';
import assert from 'node:assert/strict';
import { ProgressionProfile, HallOfFame } from '../src/game/progression/index.js';

test('saves reached level and status', () => {
  const p = new ProgressionProfile('Player');
  p.update({ level: 4, status: 'checkpoint', score: 1200 });
  const save = p.save();
  assert.equal(save.level, 4);
  assert.equal(save.status, 'checkpoint');
  assert.equal(save.score, 1200);
});

test('hall of fame requires threshold and keeps highest score', () => {
  const h = new HallOfFame({ threshold: 1000, limit: 10 });
  assert.equal(h.submit({ name: 'A', score: 999 }).eligible, false);
  assert.equal(h.submit({ name: 'A', score: 1500 }).eligible, true);
  assert.equal(h.submit({ name: 'A', score: 1200 }).eligible, true);
  assert.equal(h.list()[0].score, 1500);
});
