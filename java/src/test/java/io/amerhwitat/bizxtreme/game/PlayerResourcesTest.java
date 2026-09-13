package io.amerhwitat.bizxtreme.game;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

class PlayerResourcesTest {
    @Test void healthAmmoAndCheckpointFlow() {
        PlayerResources p = new PlayerResources();
        assertEquals(100, p.health());
        assertEquals(30, p.ammo());
        assertEquals(120, p.reserveAmmo());
        p.takeDamage(100);
        assertEquals("health", p.purchasePrompt().kind());
        p.consumeAmmo(30);
        assertEquals("ammo", p.purchasePrompt().kind());
        PlayerCheckpoint checkpoint = p.saveCheckpoint();
        assertEquals(0, checkpoint.health());
        assertEquals(0, checkpoint.ammo());
        assertTrue(p.resumeFromCheckpoint(checkpoint));
    }
}
