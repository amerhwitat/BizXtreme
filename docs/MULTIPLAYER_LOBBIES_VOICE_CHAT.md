# Multiplayer Lobbies, Voice & Chat

## Scope
This architecture applies to every BizXtreme network-enabled game: card games and future multiplayer titles use one lobby/session contract rather than bespoke matchmaking logic.

### Lobby UX
1. Select a game.
2. Create a lobby or browse compatible public lobbies.
3. Invite friends by application player ID.
4. Join the queue when seats are full.
5. Display active players across the top of the game surface.
6. Display queued players below them with queue position and matchmaking priority.
7. Admit the next eligible queued player when a seat becomes available.

### Disconnect and round replacement
The authoritative server/host owns the timer. A lost connection enters `Disconnected`. During the grace period the player can reconnect. After expiry, the player is marked `Eliminated` and loses the current round. The current round is finalized, the next queue member is admitted, and a fresh round starts. Clients cannot award a loss locally.

### Voice
Voice is an optional WebRTC audio channel. Users explicitly grant microphone permission and can mute/deafen themselves. WebRTC provides encrypted media/data transports; signaling remains under the application's authenticated session protocol. citeturn0search0turn0search10

### Chat
Chat uses the authenticated lobby/game connection, with message IDs, sequence numbers, rate limiting, moderation hooks, mute/block controls, and server timestamps. WebSocket provides standardized bidirectional communication suitable for interactive games and multi-user applications. citeturn0search2

### Privacy
Presence uses application-scoped IDs and display names. Do not expose another player's raw IP address or precise location in the UI. Voice/chat content is scoped to the current session.

### Platform implementation
Flutter uses `flutter_webrtc` for cross-platform audio/media and optional data channels. The current package supports Android, iOS, Web, macOS, Windows and Linux. citeturn0search1turn0search6
