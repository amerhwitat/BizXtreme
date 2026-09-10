# Linux Commands Source Integration

This repository now follows the Chimera II OS Linux-command integration profile.

## Upstream source families

- GNU Coreutils: `ls`, `cat`, `cp`, `mv`, `rm`, `mkdir`, text/file primitives. Upstream: https://www.gnu.org/software/coreutils/
- util-linux: `mount`, `fdisk`, `dmesg`, `lsblk`, login/system/terminal utilities. Upstream: https://github.com/util-linux/util-linux
- iproute2/net-tools: modern and legacy networking interfaces such as `ip`, `ss`, `tc`, `ifconfig`, `netstat`, `route`.
- sudo: privilege-transition tooling. Upstream: https://github.com/sudo-project/sudo
- Bash/other POSIX shells: shell language and built-ins.
- Toybox: compact command-line implementation under 0BSD, useful as a permissive reference for embedded/minimal environments.

## Integration rule

Upstream repositories are treated as source references or separately vendored dependencies. Their copyright, SPDX identifiers, tests, and build systems remain intact. Chimera-specific code is written as adapters rather than silently copying incompatible code.

## Performance profile

Prefer parallel execution only where operations are independent. Use bounded worker pools, asynchronous I/O, batching, zero-copy paths where safe, and deterministic single-threaded fallbacks. Never trade command semantics, ordering, security, or filesystem consistency for speculative parallelism.

## Two Chimera targets

1. **Standalone:** native command implementations/adapters exposed through the Koronos userland/VFS/Spotnik environment.
2. **Web UI:** the same command registry and capability model exposed through Aurora Web UI, with terminal sessions isolated from the browser and privileged operations explicitly authorized.

The detailed command registry and source acquisition workflow live in the ChimeraIIOS repository.
