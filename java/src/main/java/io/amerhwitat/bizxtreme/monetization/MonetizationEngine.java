package io.amerhwitat.bizxtreme.monetization;

import java.util.*;

public final class MonetizationEngine {
    public record Product(String type, double price, String period) {}
    public record Event(String type, String id, String provider, double amount, boolean testMode) {}
    public record Result(boolean ok, String id, String provider, double amount, String status) {}
    public static final Map<String, Product> PRODUCTS = Map.of(
        "starter_pack", new Product("consumable", 0.99, null),
        "builder_pack", new Product("consumable", 4.99, null),
        "tycoon_premium", new Product("non_consumable", 9.99, null),
        "vip_monthly", new Product("subscription", 4.99, "month"));
    private final boolean testMode;
    private final List<Event> events = new ArrayList<>();
    private final Set<String> entitlements = new HashSet<>();
    public MonetizationEngine(boolean testMode) { this.testMode = testMode; }
    public Result purchase(String productId, String provider) {
        Product p = PRODUCTS.get(productId);
        if (p == null) return new Result(false, productId, provider, 0, "unknown-product");
        events.add(new Event("purchase", productId, provider, p.price(), testMode));
        if (!p.type().equals("consumable")) entitlements.add(productId);
        return new Result(true, productId, provider, p.price(), "verification-required");
    }
    public Result recordAdImpression(String placement, String provider) { events.add(new Event("ad_impression", placement, provider, 0, testMode)); return new Result(true, placement, provider, 0, "recorded"); }
    public Result grantRewardedAd(String placement, String reward) {
        if (!placement.startsWith("rewarded_")) return new Result(false, placement, "", 0, "not-rewarded-placement");
        events.add(new Event("rewarded_ad:" + reward, placement, "", 0, testMode)); return new Result(true, placement, "", 0, "granted");
    }
    public List<Event> events() { return List.copyOf(events); }
    public Set<String> entitlements() { return Set.copyOf(entitlements); }
}
