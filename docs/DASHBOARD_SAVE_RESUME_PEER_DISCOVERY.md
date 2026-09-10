# BizXtreme Dashboard, Persistence, Hall of Fame and Peer Discovery

## Dashboard

The game dashboard is the command center for the current expedition. Its KPI vocabulary is shared across the Three.js and Unity clients:

- Score
- XP
- Expedition progress
- Play time
- Connected peer count
- Best rank

The visual treatment follows the Aurora glass/neon art direction already used by BizXtreme.

## Save / resume

Three.js uses IndexedDB with an immediate localStorage mirror for shutdown resilience. Unity uses a versioned `PlayerPrefs` JSON snapshot. Autosave is every 30 seconds in the browser client. A snapshot includes schema version, chapter, score, XP, expedition progress, play time, and UTC save time.

A future authenticated cloud-save service may replicate the same schema. Local save remains usable offline.

## Hall of Fame

The local Hall of Fame keeps the best 100 records and is available offline. A global competitive leaderboard must use an authenticated/signed submission service; peer clients are not trusted as authoritative score databases.

## Peer discovery

The game supports **opt-in** user discovery. A directory can return pseudonymous peer IDs, display names, capabilities, last-seen timestamps and a network hint. The client deliberately does not persist raw IP addresses.

WebRTC data channels support bidirectional peer-to-peer application data, while signaling/ICE exchange remains necessary to establish connections.

The application therefore does not scan the public Internet for arbitrary users or devices. It searches an application directory containing users who explicitly opted in.

## Splash screen

The Aurora Frontier splash combines three Library references:

- Aurora Wayland Glass Desktop
- Chimera II OS Aurora Showcase
- Aurora Wayland Desktop Showcase

The generated PNG is now packaged in the BizXtreme repository at:

- `threejs/assets/splash/bizxtreme-splash.png`
- `Assets/Resources/BizXtremeSplash.png`

The Three.js client displays the image during startup and Unity's `BizXSplashScreen` loads the same logical asset from Resources.

The visual language was also informed by current futuristic exploration/game UI references: atmospheric aurora/frost themes, concise launch screens, mission dashboards, progress indicators and leaderboard surfaces. External references were used as design inspiration rather than copied artwork.

The original generated splash is also retained in the user's Library as the canonical packaging source.
