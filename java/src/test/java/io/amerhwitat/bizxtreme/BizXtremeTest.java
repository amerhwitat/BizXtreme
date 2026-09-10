package io.amerhwitat.bizxtreme;

import io.amerhwitat.bizxtreme.core.BizXtremeCore;
import io.amerhwitat.bizxtreme.wallet.WalletProvider;
import org.junit.jupiter.api.Test;
import java.util.List;
import static org.junit.jupiter.api.Assertions.assertEquals;

class BizXtremeTest {
    @Test void reportsJavaRuntime() { assertEquals("java", new BizXtremeCore().health().get("runtime")); }
    @Test void forwardsWalletRequest() { var w = new WalletProvider(r -> r.method()); assertEquals("eth_chainId", w.request("eth_chainId", List.of())); }
}
