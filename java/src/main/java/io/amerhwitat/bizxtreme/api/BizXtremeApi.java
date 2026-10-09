package io.amerhwitat.bizxtreme.api;

import io.amerhwitat.bizxtreme.core.BizXtremeCore;
import java.util.Map;

public final class BizXtremeApi {
    private final BizXtremeCore core;
    public BizXtremeApi() { this(new BizXtremeCore()); }
    public BizXtremeApi(BizXtremeCore core) { this.core = java.util.Objects.requireNonNull(core, "core"); }
    public Map<String, String> health() { return core.health(); }
}
