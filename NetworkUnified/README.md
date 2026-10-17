# NetworkUnified

Unified user-visible networking/API application for BizXtreme. It standardizes the API catalog, health/configuration reporting, local interface inventory, IP scope classification, authorization checks, and bounded TCP connectivity checks across language implementations.

## API

`GET /api/v1`, `/health`, `/config`, `/interfaces`; `POST /api/v1/classify`, `/authorize`, `/tcp-check`.

Default bind for the Python/Node API servers is `127.0.0.1:8787`. Public targets require explicit allowlisting. No Internet-wide enumeration, credential attacks, evasion, spoofing, or exploitation is included.

Implementations: Python, Node.js, TypeScript, Go, Rust, Java, C#, C++, Dart, Kotlin, Swift, PHP and Ruby.

Launch with `scripts/run.bat`, `scripts/run.ps1`, or `scripts/run.sh`; choose an implementation with `NETWORK_API_IMPL`.


## Browser GUI and CORS

A browser console is published at https://amerhwitat.github.io/apps/bizxtreme-network/index.html. It supports health/config/interface inspection, classification of a single IP address, a server-side authorization check, and one bounded TCP connection attempt. It does not scan ranges or ports.

The Python service reads `NETWORK_API_CORS_ORIGINS` as a comma-separated exact-origin allowlist. Defaults permit local development origins on ports 3000 and 5173. To opt in to the published portfolio GUI, set `NETWORK_API_CORS_ORIGINS=https://amerhwitat.github.io`. Public IP targets must also be present in `NETWORK_API_ALLOWLIST`; CORS permission is not network-target authorization. Do not use wildcard origins or test systems without permission.
