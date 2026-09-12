# BizXtreme Card Game Rules Manual

Original rules/implementation guide for the BizXtreme card-game family.

## Games
Texas Hold'em Poker, Blackjack, Klondike Solitaire, FreeCell, Hearts, Spades, Crazy Eights, War, Go Fish, Gin Rummy, Cribbage, Baccarat, Euchre, Canasta, Pinochle and Old Maid.

## Architecture
Every game has a rules module, deterministic state model, legal-action validator, serializer, bot policy boundary and multiplayer transport boundary. Game state is separate from rendering, so the same rules can power desktop, web, Flutter, Kotlin and other front ends.

## Solo mode
The system supplies rule-valid opponents. Difficulty changes decision policy rather than changing the rules, deck composition or randomness after the match begins.

## Online mode
Matches use authoritative state validation. Clients send actions, not arbitrary state. Each message carries match ID, sequence number and action intent. Private hands are only delivered to their authorized player. Reconnect uses a signed/resumable snapshot.

## Poker
Two private cards and five community cards form the available pool; the best legal five-card poker hand wins the showdown. Betting is play-money only.

## Blackjack
Reach or approach 21 without exceeding it. Aces are one or eleven, face cards are ten. Dealer policy is visible and configurable.

## Solitaire and FreeCell
Moves are validated against the selected variant. Seeds can be saved for reproducible deals; statistics include wins, moves and elapsed time.

## Trick-taking games
Hearts, Spades, Euchre and Pinochle model turn order, legal-follow rules, trump and scoring as explicit state transitions.

## Collection/shedding games
Crazy Eights, War, Go Fish, Old Maid, Gin Rummy, Cribbage and Canasta expose variant configuration through data rather than hardcoded UI behavior.

## Safety
Only virtual scores and chips are supported. The repository does not implement real-money wagering, deposits, withdrawals or casino settlement.

## Art
Card faces, backs, chips and splash assets are generated as original vector/style specifications or imported only when their license permits reuse. Do not replace them with copyrighted commercial card artwork without a compatible license.

See `docs/CARD_GAMES_AND_TREX.md` and the root README for external references and attribution requirements.
