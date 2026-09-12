# Lobby Protocol v1

Transport: `wss://` WebSocket for authoritative session control. WebRTC may carry voice and optional data channels after signaling.

Messages are JSON envelopes with `type`, `version`, `sessionId`, `playerId`, `sequence`, and `payload`.

Supported types:

- `invite` — direct invitation to a game lobby.
- `join_queue` — join the game's waiting queue.
- `priority_update` — matchmaking priority update.
- `ready` — player accepts the current seat.
- `presence` — active/queued/disconnected state.
- `round_start` — authoritative new round and admitted players.
- `forfeit` — disconnected player loses the current round after the grace period.
- `chat` — lobby/game text message.
- `voice_offer`, `voice_answer`, `ice_candidate` — WebRTC signaling metadata.
- `leave` — voluntary departure.

The server validates sequence numbers, player turn, seat ownership and legal game actions. Clients never decide that another client has lost. Voice uses explicit microphone permission; chat is rate-limited and moderation-ready.
