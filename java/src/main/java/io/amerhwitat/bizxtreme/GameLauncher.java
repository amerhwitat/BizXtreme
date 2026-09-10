package io.amerhwitat.bizxtreme;

import io.amerhwitat.bizxtreme.api.BizXtremeApi;

/** Single Java entry point for starting the BizXtreme game/application. */
public final class GameLauncher {
    private GameLauncher() {}

    public static void main(String[] args) {
        BizXtremeApi api = new BizXtremeApi();
        System.out.println("BizXtreme game starting");
        System.out.println(api.health());
    }
}
