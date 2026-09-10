# BizXtreme Dashboard, Persistence, Hall of Fame and Peer Discovery

## Dashboard

The game dashboard is the command center for the current expedition. Its KPI vocabulary is shared across the Three.js and Unity clients:

- Score
- XP
- Expedition progress
- Play time
- Connected peer count
- Best rank

This follows established game-dashboard patterns where mission/progression and leaderboard information are surfaced together. The visual treatment follows the Aurora glass/neon art direction already used by BizXtreme.

## Save / resume

Three.js uses IndexedDB with a localStorage fallback. Unity uses a versioned `PlayerPrefs` JSON snapshot. Autosave is every 30 seconds in the browser client. A snapshot includes schema version, chapter, score, XP, expedition progress, play time, and UTC save time.

A future authenticated cloud-save service may replicate the same schema. Local save remains usable offline.

## Hall of Fame

The local Hall of Fame keeps the best 100 records and is available offline. A global competitive leaderboard must use an authenticated/signed submission service; peer clients are not trusted as authoritative score databases.

## Peer discovery

The game supports **opt-in** user discovery. A directory can return pseudonymous peer IDs, display names, capabilities, last-seen timestamps and a network hint. The client deliberately does not persist raw IP addresses.

This is important because WebRTC is peer-to-peer for data transport, but peers still need signaling/ICE exchange to establish connections. citehttps://developer.mozilla.org/en-US/docs/Web/API/WebRTC_API/Using_data_channels

The application therefore does not scan the public Internet for arbitrary users or devices. It searches an application directory containing users who explicitly opted in.

## Splash screen

The Aurora Frontier splash combines three Library references:

- Aurora Wayland Glass Desktop
- Chimera II OS Aurora Showcase
- Aurora Wayland Desktop Showcase

The packaged target is `BizXtremeSplash.png`. The Three.js client loads `threejs/assets/splash/bizxtreme-splash.png`; Unity loads `Resources/BizXtremeSplash`.

The visual language is informed by current futuristic exploration/game UI patterns: atmospheric aurora/frost themes, concise launch screens, mission dashboards, progress indicators and leaderboard surfaces. External references were used as design inspiration rather than copied artwork.

## Binary asset packaging limitation

The generated PNG has been prepared from the user's Library artwork, but the current repository text-content connector does not expose a binary GitHub upload operation. The repository therefore contains the asset contract and startup loaders, while the generated PNG remains separately available for the release packaging step.
