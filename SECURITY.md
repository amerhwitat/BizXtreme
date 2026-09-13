# Security policy

Never commit private keys, passwords, recovery phrases, tokens or production credentials.

Networking uses encrypted/authenticated transports for remote sessions where supported. Dynamic routing and SDN capabilities are opt-in and must not silently modify host routing state.

Uploaded avatars are untrusted image data: accept only configured image formats, enforce byte/pixel limits and normalize before rendering.

Do not place wallet secrets, raw IP addresses or exact location in profiles, saves, logs, telemetry or P2P messages.
