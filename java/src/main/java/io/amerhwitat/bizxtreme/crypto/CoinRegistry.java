package io.amerhwitat.bizxtreme.crypto;

import java.util.Map;
import java.util.concurrent.ConcurrentHashMap;

public final class CoinRegistry {
    private final Map<String, String> chains = new ConcurrentHashMap<>();
    public void register(String symbol, String network) { chains.put(symbol, network); }
    public String network(String symbol) { return chains.get(symbol); }
}
