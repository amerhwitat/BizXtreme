package io.amerhwitat.bizxtreme.monetization;

import java.util.*;

public final class MonetizationEngine {
    public record Product(String type, double price, String period) {}
    public record Event(String type, String id, String provider, double amount, boolean testMode) {}
    public record PaymentTarget(String asset, String recipient, String account) {}
    public record PaymentRouting(PaymentTarget ethereum, PaymentTarget paypal, String defaultMethod, String fallbackMethod, boolean requiresExplicitUserSelection) {}
    public record Result(boolean ok, String id, String provider, double amount, String status, PaymentRouting paymentRouting) {}
    public static final Map<String, Product> PRODUCTS = Map.ofEntries(
        Map.entry("starter_pack", new Product("consumable", 0.99, null)), Map.entry("builder_pack", new Product("consumable", 4.99, null)),
        Map.entry("tycoon_premium", new Product("non_consumable", 9.99, null)), Map.entry("vip_monthly", new Product("subscription", 4.99, "month")),
        Map.entry("medical_kit", new Product("consumable", 0.49, null)), Map.entry("ammo_pack", new Product("consumable", 0.29, null)), Map.entry("survival_bundle", new Product("consumable", 0.69, null)));
    private static final PaymentRouting PAYMENT_ROUTING = new PaymentRouting(new PaymentTarget("ETH", "0x0B4fF3fc6AE19fAF9A0d2628a646ABD9636B1162", null), new PaymentTarget(null, null, "amer.hwaitat@gmail.com"), "ethereum", "paypal", true);
    private final boolean testMode; private final List<Event> events = new ArrayList<>(); private final Set<String> entitlements = new HashSet<>();
    public MonetizationEngine(boolean testMode) { this.testMode = testMode; }
    public Result purchase(String productId, String provider) { Product p=PRODUCTS.get(productId); if(p==null)return new Result(false,productId,provider,0,"unknown-product",PAYMENT_ROUTING); events.add(new Event("purchase",productId,provider,p.price(),testMode)); if(!p.type().equals("consumable"))entitlements.add(productId); return new Result(true,productId,provider,p.price(),"verification-required",PAYMENT_ROUTING); }
    public Result recordAdImpression(String placement,String provider){events.add(new Event("ad_impression",placement,provider,0,testMode));return new Result(true,placement,provider,0,"recorded",PAYMENT_ROUTING);}
    public Result grantRewardedAd(String placement,String reward){if(!placement.startsWith("rewarded_"))return new Result(false,placement,"",0,"not-rewarded-placement",PAYMENT_ROUTING);events.add(new Event("rewarded_ad:"+reward,placement,"",0,testMode));return new Result(true,placement,"",0,"granted",PAYMENT_ROUTING);}
    public List<Event> events(){return List.copyOf(events);} public Set<String> entitlements(){return Set.copyOf(entitlements);}
}
