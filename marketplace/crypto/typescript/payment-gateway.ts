export type PaymentMode = 'free' | 'crypto_testnet' | 'crypto_mainnet_provider';

export interface CatalogItem {
  asset_id: string;
  free: boolean;
  fiat_price_minor: number;
  currency: string;
  accepted_payment_methods: PaymentMode[];
}

export interface PaymentIntent {
  order_id: string;
  asset_id: string;
  fiat_price_minor: number;
  currency: string;
  mode: PaymentMode;
}

export interface PaymentVerification {
  accepted: boolean;
  already_processed: boolean;
  transaction_id: string;
  reason?: string;
}

export interface PaymentGateway {
  verify(intent: PaymentIntent, transactionId: string): Promise<PaymentVerification>;
}

export function validatePurchase(item: CatalogItem, intent: PaymentIntent): string | null {
  if (intent.asset_id !== item.asset_id) return 'asset_mismatch';
  if (intent.fiat_price_minor !== item.fiat_price_minor) return 'price_mismatch';
  if (intent.currency !== item.currency) return 'currency_mismatch';
  if (!item.accepted_payment_methods.includes(intent.mode)) return 'payment_method_not_allowed';
  if (intent.mode !== 'free' && item.free) return 'free_item_should_not_require_payment';
  return null;
}
