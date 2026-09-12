# Flutter Voice & Chat

`SessionChannels` is the application state layer. Production transport should connect it to authenticated WSS signaling and `flutter_webrtc` media sessions.

The `flutter_webrtc` package currently supports audio/video and data channels across Android, iOS, Web, macOS, Windows and Linux. citeturn0search1turn0search6

Microphone permission is opt-in. Default microphone state is muted. Chat is text-only and session-scoped. The game server remains authoritative for game actions and disconnect forfeits.
