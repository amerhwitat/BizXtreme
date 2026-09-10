# BizXtreme Social, Avatar, NFT, and Emoji Expansion

## Status
Approved architecture for the next implementation phase.

## Goals
- Expand the game with additional story chapters and collectible editions.
- Add purchasable player avatars and an in-game avatar selection system.
- Add optional blockchain-linked collectible ownership without custody of user secrets.
- Add multiplayer peer-to-peer chat using WebRTC data channels with a separate signaling service.
- Add a canonical Unicode emoji importer for game chat and UI, using Unicode data files rather than scraping arbitrary artwork.
- Keep Unity and Three.js clients aligned through shared content schemas.

## Scope
### 1. Story and collectible content
Add new chapters/events and collectible metadata under the existing `game/content` and `game/catalog` trees. Content is data-driven and platform-neutral. NFT metadata is descriptive and does not contain private keys or seed material.

### 2. Avatar system
Define a shared avatar schema containing stable id, display name, rarity, cosmetic slots, preview asset references, unlock/purchase state, and compatibility flags. Unity receives a C# model; Three.js consumes JSON/module data. Player identity remains separate from wallet identity.

Initial avatar families:
- Frontier Ranger
- Aurora Pilot
- Signal Seeker
- Black Aurora
- Expedition Commander
- Frontier Guardian
- Supply Drone Companion
- Faction Envoy

### 3. NFT/ownership boundary
Support unique collectibles through ERC-721-compatible metadata and edition/multi-token concepts through ERC-1155-compatible metadata. The game never requests or stores a seed phrase/private key. Ownership verification is read-only where possible; purchases use an explicit wallet-provider signing flow and a fixed merchant destination already defined by the project. No sweeping, draining, key recovery, or address-to-private-key recovery is part of this feature.

State flow:
`Catalog -> Quote -> Fixed merchant destination -> Wallet provider -> User signs -> Broadcast -> Verify -> Confirm -> Grant`

Granting is idempotent and only follows verified transaction state.

### 4. Peer-to-peer chat
Use WebRTC `RTCDataChannel` for bidirectional peer-to-peer text/chat payloads. Signaling is intentionally separate from chat transport and exchanges SDP/ICE information. The protocol includes:
- room/player identifiers
- bounded message size
- rate limits
- sequence numbers and timestamps
- reconnect/peer lifecycle
- mute/block/report controls
- client-side moderation hooks
- no transmission of wallet secrets

STUN/TURN configuration is supported for peers that cannot establish a direct route.

### 5. Emoji ingestion
Use the current Unicode emoji data distribution as the canonical repertoire. Import structured data such as emoji-data, emoji-sequences, emoji-ZWJ-sequences, and emoji-test into a versioned generated catalog. Do not claim to import every third-party emoji image on the internet. Rendering uses properly licensed fonts/assets, with fallback behavior for unsupported glyphs.

### 6. Cross-client integration
Three.js and Unity use the same logical content identifiers and JSON-compatible schemas. Existing game content remains backward compatible. The Three.js client should consume `src/game/content.js` rather than duplicate catalog data in `main.js`.

## Error handling and security
- Invalid or stale ownership proofs are rejected without granting items.
- Network failures never imply successful purchase.
- Duplicate transaction notifications do not duplicate grants.
- Signaling messages are validated and bounded.
- Chat input is escaped/sanitized before rendering.
- Blocked peers are prevented from initiating normal chat sessions where the client can enforce it.
- Wallet provider errors are surfaced without exposing secrets.

## Testing
- JSON/schema validation for stories, avatars, catalog, and emoji data.
- Unit tests for avatar lookup, ownership verification state transitions, chat message validation, rate limiting, and idempotent grants.
- Browser tests for WebRTC feature detection and fallback behavior.
- Unity tests for serialization and avatar selection.
- Three.js build/lint tests and integration tests for shared content imports.
- CI must report actual pass/fail results; no platform build is considered complete without evidence.

## Non-goals
- Private-key/seed recovery or guessing.
- Wallet sweeping/draining.
- Scraping copyrighted third-party emoji artwork.
- Treating WebRTC as serverless: signaling remains required.
- Claiming Unity WebGL is equivalent to native mobile builds.
