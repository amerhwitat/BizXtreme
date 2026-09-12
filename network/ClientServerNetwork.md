# BizXtreme Client / Server / P2P Network Module

BizXtreme networking is a unified application feature rather than a separate launcher. Existing P2P/presence functionality can run beside client/server rooms and services.

## Modes

- Client — connect to a remote host.
- Server — host rooms and application services.
- Host — server + local client in one running application.
- P2P — direct peer links where supported.
- Hybrid — authoritative server plus selected direct peer channels.

## Profile and avatars

The Network Center asks for a nickname and avatar. Built-in avatars are selectable. When no suitable built-in avatar is available, `Upload avatar` opens local storage. Validate PNG/JPEG/WebP, enforce size and decoded-pixel limits, normalize the image and remove unnecessary metadata before storing it.

## Platform adapters

The same protocol is exposed to Visual C++, C#/WPF, Unity, Unreal, Node.js, Java, Python, JavaScript, TypeScript, Kotlin, Flutter/Dart and Swift layers. Browser builds should prefer WebRTC for direct peers and WebSocket/WebTransport for client/server connectivity.

## Host mode invariant

The host's local player is a normal client of the embedded server. Server-side authorization, state synchronization and event routing are therefore exercised locally and remotely through the same code path.

## Security

Never send wallet keys, seed phrases, passwords, private save data or unrelated OS credentials. Do not expose raw IP addresses as profile information.
