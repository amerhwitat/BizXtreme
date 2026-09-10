import test from 'node:test';
import assert from 'node:assert/strict';
import { createBizXtreme } from '../src/index.js';

test('BizXtreme reports healthy Node.js runtime', () => {
  assert.deepEqual(createBizXtreme().health(), {
    name: 'BizXtreme',
    version: '1.0.0',
    status: 'ok',
    runtime: 'node'
  });
});
