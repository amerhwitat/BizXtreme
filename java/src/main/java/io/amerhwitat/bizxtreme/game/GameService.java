package io.amerhwitat.bizxtreme.game;

import java.util.Map;
import java.util.concurrent.ConcurrentHashMap;

public final class GameService {
    private final Map<String, String> saves = new ConcurrentHashMap<>();
    public void save(String slot, String state) { saves.put(slot, state); }
    public String load(String slot) { return saves.get(slot); }
}
