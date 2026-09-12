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
The preferred deck is the license-verified OpenDecks Public Domain / CC0 deck. Fetch it with the platform script under `mobile/flutter/scripts/`, preserve its license/readme, and retain the programmatic fallback. Do not mix sources silently: every imported pack must have source/license/checksum metadata.

## QA and release
Validate every variant's scoring and edge cases; test both cached-art and fallback-art paths; run platform-specific build scripts; inspect dependency and asset licenses before release.

## Asset references
- OpenDecks CC0 deck: https://github.com/AustinGabriel/OpenDecks-Public-Domain-and-CC0-Playing-Cards
- Kenney Playing Cards Pack: https://kenney.nl/assets/playing-cards-pack
- OpenGameArt Cards: https://opengameart.org/content/cards-0
