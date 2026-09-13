package io.amerhwitat.bizxtreme.game;
import io.amerhwitat.bizxtreme.monetization.MonetizationEngine;
import java.util.HashMap; import java.util.Map;
public final class TycoonGame {
    public static final String PRIMARY_ETH_ADDRESS = "0x0B4fF3fc6AE19fAF9A0d2628a646ABD9636B1162";
    public static final String PRIMARY_PAYPAL_ACCOUNT = "amer.hwaitat@gmail.com";
    private static final Map<String,Business> BUSINESSES = Map.of("bakery",new Business("Bakery",900,300),"market",new Business("Market",1500,650),"factory",new Business("Factory",2600,1200));
    private long cash; private int turn; private final Map<String,Integer> owned=new HashMap<>(); private final MonetizationEngine monetization=new MonetizationEngine(true);
    public TycoonGame(long cash){this.cash=cash;} public long cash(){return cash;}
    public PurchaseResult buyBusiness(String type,long price){if(price<=0||cash<price||!BUSINESSES.containsKey(type))return new PurchaseResult(false,null);cash-=price;owned.merge(type,1,Integer::sum);return new PurchaseResult(true,new Payment("ETH",PRIMARY_ETH_ADDRESS,PRIMARY_PAYPAL_ACCOUNT,price,"wallet-authorization-required"));}
    public MonetizationEngine.Result purchasePack(String productId,String provider){return monetization.purchase(productId,provider);}
    public MonetizationEngine.Result recordAd(String placement,String provider){return monetization.recordAdImpression(placement,provider);}
    public MonetizationEngine.Result claimRewardedIncome(long amount){var r=monetization.grantRewardedAd("rewarded_double_income","cash:"+amount);if(r.ok()&&amount>0)cash+=amount;return r;}
    public TurnResult advanceTurn(){long revenue=0,costs=0;for(var e:owned.entrySet()){var b=BUSINESSES.get(e.getKey());revenue+=b.revenue()*e.getValue();costs+=b.costs()*e.getValue();}cash+=revenue-costs;turn++;return new TurnResult(turn,revenue,costs,revenue-costs,cash);}
    private record Business(String name,long revenue,long costs){}
}
record Payment(String asset,String recipient,String paypalAccount,long amount,String status){} record PurchaseResult(boolean ok,Payment payment){} record TurnResult(int turn,long revenue,long costs,long profit,long cash){}
