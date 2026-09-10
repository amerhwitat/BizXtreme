package io.amerhwitat.bizxtreme.wallet;

import java.util.List;
import java.util.Objects;
import java.util.function.Function;

public final class WalletProvider {
    private final Function<Request, Object> provider;
    public WalletProvider(Function<Request, Object> provider) { this.provider = Objects.requireNonNull(provider); }
    public Object request(String method) { return request(method, List.of()); }
    public Object request(String method, List<Object> params) { return provider.apply(new Request(method, params)); }
    public record Request(String method, List<Object> params) {}
}
