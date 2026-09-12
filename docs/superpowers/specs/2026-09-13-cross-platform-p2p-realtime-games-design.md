# Cross-Platform P2P Realtime Games Design

## Goal

Enable desktop, web, Android/iOS, and other supported clients to play the same networking games together in real time, with a common protocol, peer-to-peer transport where feasible, relay fallback where direct connectivity is impossible, synchronized game state, voice/chat, audio events, randomized backgrounds, reconnect/forfeit handling, and reproducible public web releases.

## Architecture

- **Authoritative session model:** one elected/assigned host or lightweight authoritative session service validates game actions, sequence numbers, turns, round transitions, queue admission, disconnect grace periods, and forfeits. Clients never decide another player's loss locally.
- **P2P transport:** WebRTC data channels for low-latency peer traffic; authenticated WebSocket/WSS signaling for session discovery, SDP/ICE exchange, presence, and fallback control traffic.
- **Connectivity:** STUN for NAT discovery and TURN relay fallback when direct P2P fails. Transport capability negotiation determines whether a client uses WebRTC, WebSocket relay, or a local/offline adapter.
- **Protocol:** versioned JSON/binary-compatible envelope with session ID, peer ID, sequence, timestamp/round, message type, and payload. Duplicate/reordered messages are rejected or reconciled deterministically.
- **Cross-platform compatibility:** platform-neutral protocol plus native adapters for C++, C#, Java, Kotlin, Python, Node.js, JavaScript, TypeScript, Swift, and Dart/Flutter where present.

## Game lifecycle

`discover -> invite -> lobby -> priority queue -> ready -> synchronized round start -> real-time play -> disconnect grace/reconnect -> forfeit if grace expires -> next round -> queue admission -> session end -> result/summary`

## Audio/event system

Create a shared event catalog covering lobby, gameplay, turn, timer, card/deck, player presence, chat/voice, win/loss/draw, streak/achievement, disconnect/forfeit, round end, and session end events. Each event has a sound ID, priority, cooldown, local-player relevance, and fallback behavior. Licensed external audio must retain source/license metadata; generated/programmatic effects are preferred.

## Visual background system

Provide multiple licensed/public-domain/CC0 backgrounds per game/theme, source metadata, local fallback artwork, random shuffle, optional deterministic session seed, preloading, caching, and accessibility-safe contrast. External assets are never required for a game to start.

## Synchronization and resilience

- Sequence-numbered actions and periodic authoritative snapshots.
- Client prediction only for non-authoritative presentation; authoritative correction for game state.
- Heartbeats and connection quality indicators.
- Reconnect tokens scoped to a session and peer identity.
- Grace timer followed by authoritative forfeit.
- Deterministic round reset and queue admission.
- Voice defaults muted until explicit permission/enablement.
- Chat rate limits, mute/block hooks, and moderation extension points.
- Wallet keys and secrets never enter P2P traffic.

## Web/mobile/desktop requirements

Web clients must run from HTTPS and use browser WebRTC APIs. Mobile clients require microphone/network permissions only when needed. Desktop clients use the same protocol and can fall back to relay mode. No client may expose raw peer IPs in player-facing UI or persistent profiles.

## Testing

Add protocol conformance tests, queue/priority tests, reconnect and race-condition tests, deterministic background tests, audio-event mapping tests, malformed/duplicate packet tests, capability negotiation tests, and cross-client interoperability fixtures.

## Public deployment

- GitHub is the canonical source and release host.
- GitHub Pages publishes static documentation/web builds.
- Cloudflare Pages may automatically deploy the web client from GitHub and provide preview deployments.
- itch.io is a target for browser-playable HTML5 game packages.
- Deployment workflows must publish only verified build artifacts and must not fabricate deployment URLs.

## Security and privacy

Use authenticated signaling, session-scoped identities, replay protection, input validation, rate limiting, and explicit permissions. Never transmit wallet secrets, recovery phrases, raw IPs, or exact location through game/presence protocols.

## Acceptance criteria

A supported desktop, browser, and mobile client can join the same session, negotiate compatible transport, synchronize the same round state, exchange real-time game actions, use optional voice/chat, survive transient disconnects, apply the same authoritative win/loss outcome, and start the next round with the queued player without divergent state. Web publishing is reproducible from repository workflows and deployment status is verifiable after publication.
