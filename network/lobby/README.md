# Multiplayer Lobby

All networked games use the same session lifecycle: **invite → lobby → priority queue → ready → playing → disconnect/forfeit → next round**.

## Player ordering
The lobby displays active players at the top of the game. Queued players are ordered by explicit matchmaking priority and then FIFO join time. Priority is a matchmaking value, not a payment or gambling advantage.

## Disconnect policy
A playing client enters `Disconnected` on transport loss. After the configured grace period, the authoritative host/server marks that player `Eliminated` for the current round. The round is finalized, then the next queued player is admitted and a new round begins. Reconnection may restore presence only before the forfeit deadline.

## Communication
- **Game channel:** authoritative state/actions over WSS/WebSocket.
- **Chat channel:** text messages with moderation/rate limits.
- **Voice channel:** WebRTC audio with explicit microphone permission and mute/deafen controls.

WebSocket is appropriate for reliable bidirectional lobby/game messaging; WebRTC data channels and media tracks provide peer communication for low-latency data and voice. See RFC 6455, RFC 8831 and the WebRTC documentation in `docs/NETWORKING.md`.

No player's IP address or precise location is exposed in the lobby UI. Player identity uses an application-scoped peer ID/display name.
