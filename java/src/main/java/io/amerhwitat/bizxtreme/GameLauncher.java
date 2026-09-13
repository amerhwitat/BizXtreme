package io.amerhwitat.bizxtreme;

import io.amerhwitat.bizxtreme.api.BizXtremeApi;
import io.amerhwitat.bizxtreme.game.TycoonGame;

/** Single Java entry point for starting BizXtreme or its Tycoon mode. */
public final class GameLauncher {
    private GameLauncher() {}
    public static void main(String[] args) {
        BizXtremeApi api = new BizXtremeApi();
        System.out.println("BizXtreme game starting");
        System.out.println(api.health());
        if (args.length > 0 && "tycoon".equalsIgnoreCase(args[0])) {
            TycoonGame game = new TycoonGame(10_000);
            System.out.println("BizXtreme Tycoon ready: cash=" + game.cash());
        }
    }
}
