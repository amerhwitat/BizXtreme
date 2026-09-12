# Card artwork sources and integration

## Primary artwork

The game suite now uses the **OpenDecks Public Domain / CC0 Playing Cards** project as its preferred external deck. It supplies a complete 54-card deck in SVG and PNG, including backs, and is released as CC0/public-domain material.

Source: https://github.com/AustinGabriel/OpenDecks-Public-Domain-and-CC0-Playing-Cards

The repository is fetched by `mobile/flutter/scripts/fetch_card_art.ps1`, `.bat`, or `.sh`. The imported cache keeps the source `LICENSE` and `README.md` beside the art.

## Additional verified sources

- Kenney Playing Cards Pack — CC0: https://kenney.nl/assets/playing-cards-pack
- OpenGameArt Cards — CC0 SVG: https://opengameart.org/content/cards-0
- OpenGameArt Bridge-Sized Playing Card Deck — CC0 PNG: https://opengameart.org/content/bridge-sized-playing-card-deck-png-cc0

These are alternates; they are not silently mixed into the primary deck.

## Runtime policy

1. Prefer locally cached licensed artwork.
2. Fall back to programmatic/vector cards when the cache is absent.
3. Never fetch arbitrary images at runtime without a license record.
4. Preserve source, license, attribution status and checksum when a pack is vendored.
5. Do not treat free-to-download as automatically free-to-reuse.

## Implementation

`mobile/flutter/lib/games/card_art.dart` resolves the external deck and supplies the fallback renderer. The card model exposes `assetRank` so game logic and presentation remain separate.

## Legal/maintenance note

License metadata is checked when sources are selected, but third-party license terms can change. Refresh the source manifest before a release and retain the exact license text shipped with any vendored asset pack.
