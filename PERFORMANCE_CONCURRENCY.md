# Performance & Concurrency Policy

BizXtreme components should use bounded concurrency for independent requests, I/O, background jobs, and data transformations.

- Prefer asynchronous I/O for network-bound work.
- Use bounded worker pools for CPU-heavy independent jobs.
- Avoid unbounded task creation and nested pools.
- Keep shared state synchronized or isolated per worker.
- Preserve ordering where APIs require it.
- Keep a deterministic low-concurrency mode for tests.
- Measure throughput, latency, memory, and contention before/after changes.
