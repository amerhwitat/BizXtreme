import test from 'node:test';
import assert from 'node:assert/strict';
import { createWalletProvider } from '../src/index.js';

test('wallet provider forwards JSON-RPC requests', async () => {
  const calls = [];
  const wallet = createWalletProvider({ request: async payload => { calls.push(payload); return '0x1'; } });
  assert.equal(await wallet.request('eth_chainId'), '0x1');
  assert.deepEqual(calls, [{ method: 'eth_chainId', params: [] }]);
});
