export class WalletProvider {
  constructor(provider) { this.provider = provider; }

  async request(method, params = []) {
    if (!this.provider || typeof this.provider.request !== 'function') {
      throw new Error('Wallet provider does not implement request(method, params)');
    }
    return this.provider.request({ method, params });
  }
}

export function createWalletProvider(provider) {
  return new WalletProvider(provider);
}
