package io.amerhwitat.bizxtreme.game;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

class TycoonGameTest {
    @Test void purchaseUsesPrimaryEthRecipient() {
        TycoonGame game = new TycoonGame(10_000);
        PurchaseResult result = game.buyBusiness("bakery", 2_500);
        assertTrue(result.ok());
        assertEquals("0x0B4fF3fc6AE19fAF9A0d2628a646ABD9636B1162", result.payment().recipient());
        assertEquals(7_500, game.cash());
    }

    @Test void turnProducesRevenueAndCosts() {
        TycoonGame game = new TycoonGame(10_000);
        game.buyBusiness("bakery", 2_500);
        long before = game.cash();
        TurnResult result = game.advanceTurn();
        assertTrue(result.revenue() > 0);
        assertTrue(result.costs() > 0);
        assertEquals(before + result.revenue() - result.costs(), game.cash());
    }
}
