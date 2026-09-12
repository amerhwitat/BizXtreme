# BizXtreme Peer Presence & P2P Policy

Presence is consent-based. Store a random peer ID and connection state rather than permanent IP addresses. Do not expose raw IP addresses to other players. If infrastructure necessarily sees an IP, treat it as operational/security telemetry with explicit retention rules.

Never derive or publish a player's exact location from IP. Players can optionally select a coarse region label. Exact GPS is never shared by default.

Live presence: peer ID, display name, connected/disconnected, last-seen timestamp, optional coarse region. Provide disable/delete controls. Wallet seed phrases, private keys, backup material and secret save data are prohibited from P2P channels.
