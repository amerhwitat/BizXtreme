from dataclasses import dataclass

@dataclass(frozen=True)
class CatalogItem:
    asset_id: str
    free: bool
    fiat_price_minor: int
    currency: str = "USD"

@dataclass(frozen=True)
class PaymentIntent:
    order_id: str
    asset_id: str
    fiat_price_minor: int
    currency: str
    mode: str

ALLOWED_MODES = {"free", "crypto_testnet", "crypto_mainnet_provider"}


def validate_purchase(item: CatalogItem, intent: PaymentIntent) -> str | None:
    if intent.mode not in ALLOWED_MODES:
        return "payment_mode_not_allowed"
    if intent.asset_id != item.asset_id:
        return "asset_mismatch"
    if intent.fiat_price_minor != item.fiat_price_minor:
        return "price_mismatch"
    if intent.currency != item.currency:
        return "currency_mismatch"
    if item.free and intent.mode != "free":
        return "free_item_requires_no_payment"
    if not item.free and intent.mode == "free":
        return "paid_item_requires_verified_payment"
    return None


def credit_only_after_verified_payment(verified: bool, idempotency_key: str | None) -> bool:
    return bool(verified and idempotency_key)
