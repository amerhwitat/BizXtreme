# BizXtreme Card Games & T-Rex

## Included

- Texas Hold’em Poker
- Blackjack
- Classic Card Suite: Klondike Solitaire, FreeCell, Hearts, Spades, Crazy Eights, War
- T-Rex Runner

The launcher treats these as first-class games alongside the existing 2D/3D/4D worlds, store, wallet, save and presence menus.

## Rules and flow

Texas Hold’em: `lobby → deal → pre-flop → flop → turn → river → showdown → result → save`.

Blackjack: `table → deal → player action → dealer action → result → save`.

Classic cards share the deck and rules boundary while each game receives its own rules module. T-Rex uses `launch → run → jump → obstacle → score → hall-of-fame`.

Rules were independently reimplemented from public descriptions instead of copying third-party source code. References: https://bicyclecards.com/how-to-play/texas-holdem-poker and https://bicyclecards.com/how-to-play/blackjack/.

## Original artwork

`mobile/flutter/assets/art/splash.svg` and `card_deck.svg` are original vector artwork created for BizXtreme. The card UI is data-driven so all 52 standard cards can be rendered consistently at any resolution.

## Multiplayer

The UI exposes single-player and online-multiplayer mode selection. The production transport is intentionally an adapter: WebSocket/WebRTC/libp2p implementations can be added without coupling game rules to network code. Presence remains consent-based; raw IP addresses are not exposed to players or persisted in profiles, and exact location is never inferred from an IP address.

## Wallet boundary

Game state can reference a wallet provider/account label, but private keys and recovery phrases never enter saves, screenshots, logs, telemetry or peer messages. Real-money wagering is outside this game engine.

## Mobile architecture sources

Flutter's official Casual Games Toolkit provides a card-game template and multiplayer hooks; Flame provides the real-time 2D engine model; Kotlin Multiplatform supports shared Android/iOS logic.

- https://docs.flutter.dev/resources/games-toolkit
- https://flutter.dev/blog/building-your-next-casual-game-with-flutter
- https://kotlinlang.org/multiplatform/

## Asset provenance

Third-party assets require explicit license metadata. Public availability alone is not treated as a redistribution license. Imported assets must retain source, license, attribution and integrity metadata.
