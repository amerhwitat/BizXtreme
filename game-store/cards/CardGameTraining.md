# BizXtreme Card Games Developer Training Manual

## Shared architecture
Rules, state, AI, networking, persistence and rendering are separate layers. This permits one rules implementation to drive Flutter, Kotlin, web and native clients.

## Rules
Use immutable or controlled state transitions. Every action is checked against the current phase, player turn, private information and variant configuration.

## Randomness
Inject the random source. Save the match seed and state hash for replay/debugging. Never let UI code invent card results.

## Bots
Bots receive only information available to the simulated player. Difficulty is a policy parameter.

## Multiplayer
Use authoritative action validation, sequence numbers, reconnect snapshots and privacy-preserving presence. Never transmit another player's private hand to an unauthorized client.

## Art pipeline
Use original vector card faces/backs and generated decorative artwork, with an asset manifest containing source, license and checksum for imported assets. No third-party proprietary artwork is bundled merely because it is visible online.

## QA and release
Validate every variant's scoring and edge cases; run platform-specific build scripts; inspect dependency and asset licenses before release.
