#pragma once
#include <cstdint>
#include <string>

namespace bizxtreme::payments {

enum class PaymentMode { Free, CryptoTestnet, CryptoProvider };

struct CatalogItem {
    std::string asset_id;
    bool free{false};
    std::int64_t fiat_price_minor{0};
    std::string currency{"USD"};
};

struct PaymentIntent {
    std::string order_id;
    std::string asset_id;
    std::int64_t fiat_price_minor{0};
    std::string currency{"USD"};
    PaymentMode mode{PaymentMode::Free};
};

struct PaymentVerification {
    bool accepted{false};
    bool already_processed{false};
    std::string transaction_id;
    std::string reason;
};

class PaymentGateway {
public:
    virtual ~PaymentGateway() = default;
    virtual PaymentVerification verify(const PaymentIntent& intent,
                                       const std::string& transaction_id) = 0;
};

} // namespace bizxtreme::payments
