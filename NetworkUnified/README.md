# NetworkUnified

Unified user-visible networking/API application for BizXtreme. It standardizes the API catalog, health/configuration reporting, local interface inventory, IP scope classification, authorization checks, and bounded TCP connectivity checks across language implementations.

## API

`GET /api/v1`, `/health`, `/config`, `/interfaces`; `POST /api/v1/classify`, `/authorize`, `/tcp-check`.

Default bind for the Python/Node API servers is `127.0.0.1:8787`. Public targets require explicit allowlisting. No Internet-wide enumeration, credential attacks, evasion, spoofing, or exploitation is included.

Implementations: Python, Node.js, TypeScript, Go, Rust, Java, C#, C++, Dart, Kotlin, Swift, PHP and Ruby.

Launch with `scripts/run.bat`, `scripts/run.ps1`, or `scripts/run.sh`; choose an implementation with `NETWORK_API_IMPL`.
