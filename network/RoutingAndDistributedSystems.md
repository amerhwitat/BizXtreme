# BizXtreme routing and distributed-system resilience

BizXtreme keeps the network architecture layered: application sessions sit above TCP/UDP/QUIC and the host's IPv4/IPv6 routing system. P2P and client/server remain independent paths that can coexist.

## Routing capability boundary

The OS/network adapter may provide static and connected routes plus RIP/RIPng, OSPFv2/v3, IS-IS, BGP4, EIGRP compatibility, Babel, BFD, VRRP, PIM, OpenFabric and BGP-LS. SDN adapters cover OpenFlow, P4Runtime, NETCONF, RESTCONF, gNMI and Envoy xDS. FRR is treated as a standards/reference compatibility boundary, not copied source. citeturn0search6turn0search1

## Service complexity controls

- Prefer local modules for tightly coupled game/UI functions.
- Use gRPC/HTTP2 for typed native service calls and reuse channels.
- Stream long-lived multiplayer/session data instead of opening repeated RPCs. citeturn0search5
- Keep authoritative game data service-local.
- Use event versioning, idempotency and outbox/inbox processing.
- Use Saga compensation rather than distributed ACID transactions.
- Bound retries and use circuit breakers/bulkheads.
- Apply resource budgets to every process/container.
- Use canary/blue-green deployment and backwards-compatible protocol versions.

## Observability

OpenTelemetry is the standard instrumentation boundary for traces, metrics and logs. W3C trace context follows requests through service boundaries; the Collector can receive, process and export telemetry. citeturn0search9turn1search5

## Dynamic service routing

Envoy xDS can provide dynamic listeners, routes, clusters and endpoints through gRPC/REST. Static configuration remains valid for small deployments; dynamic xDS should only be introduced when service discovery/traffic policy justifies the additional control plane. citeturn1search3turn1search9
