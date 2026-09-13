# Cross-game progression, saves, Hall of Fame and onboarding

Every game implementation should use the same progression contract:

- Save reached level/chapter, current status, score, health/ammo and a resumable checkpoint.
- Autosave at safe checkpoints and on pause/quit; resume later without losing the last confirmed state.
- Ask for a display name when a player first enters a Hall of Fame.
- Each game has its own leaderboard namespace and threshold. The default threshold is 1,000 points and can be changed per game.
- Only scores meeting the configured threshold are eligible; entries are sorted highest-first and capped at 100.
- Rules appear before first start, followed by an optional skippable training/tutorial screen.
- Mobile editions use safe areas, thumb-friendly controls and touch targets of at least 44 px/dp. Left-side movement and right-side actions are the default.
- Health/ammo and other critical state are part of the same save snapshot.

The browser, Kotlin and Flutter mobile boundaries expose the same onboarding/progression concepts so individual game clients can bind their own screens without duplicating game state.
