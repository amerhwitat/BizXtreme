import 'package:flutter_test/flutter_test.dart';
import '../lib/games/card_games.dart';
void main(){test('deck contains 52 unique cards',(){final d=Deck();expect(d.cards.length,52);expect(d.cards.map((c)=>c.label).toSet().length,52);});test('blackjack ace can be 1 or 11',(){final cards=[const PlayingCard(Suit.spades,Rank.ace),const PlayingCard(Suit.hearts,Rank.six)];expect(BlackjackRound.value(cards),17);});test('poker round deals hole cards and flop',(){final r=PokerRound();r.deal();expect(r.player.length,2);expect(r.bot.length,2);expect(r.community.length,3);});}
