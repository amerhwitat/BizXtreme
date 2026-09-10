# BizXtreme multiplayer chat and avatar design

## Player avatars

The game now defines a shared avatar vocabulary for the Unity and Three.js clients. Avatars are gameplay/cosmetic identities and can be selected, unlocked, equipped, animated, and used in player profiles and chat.

Planned identities include Frontier Ranger, Aurora Pilot, Signal Seeker, Black Aurora, Expedition Commander, Frontier Guardian, Supply Drone Companion, and Faction Envoy.

Blockchain-linked collectibles, where used, must be treated as optional ownership records. The client must verify ownership before granting an entitlement and must never request a player's seed phrase or private key.

## Chat

The browser client uses WebRTC RTCDataChannel for peer-to-peer chat. A signaling layer is still required to exchange connection offers, answers, and ICE candidates; application chat messages are sent through the peer data channel after the connection is established.

Required controls:

- display name and avatar
- room/session identifier
- mute
- block
- report
- rate limiting
- message-size limits
- reconnect handling
- profanity/spam moderation hooks
- no private keys, seed phrases, or wallet secrets in chat

WebRTC data channels are encrypted in transit by the WebRTC stack.

## Emoji

Emoji support uses the Unicode Emoji data files as the canonical vocabulary instead of scraping or redistributing arbitrary third-party artwork. The importer should consume emoji-data, emoji-sequences, emoji-zwj-sequences, and emoji-test data from the Unicode release selected by the project.

This gives chat, reactions, avatar emotes, and UI access to the Unicode-defined emoji repertoire while leaving the visual rendering to a properly licensed font or emoji asset set.
