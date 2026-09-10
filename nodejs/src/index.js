export { BizXtremeCore } from './core/index.js';
export { WalletProvider, createWalletProvider } from './wallet/index.js';

export function createBizXtreme(options = {}) {
  return new BizXtremeCore(options);
}
