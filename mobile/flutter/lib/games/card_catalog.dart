class CardGameDefinition {
  final String id;
  final String title;
  final String mode;
  final String rulesBook;
  const CardGameDefinition(this.id, this.title, this.mode, this.rulesBook);
}

const cardGameCatalog = <CardGameDefinition>[
  CardGameDefinition('poker_holdem', "Texas Hold'em Poker", 'solo+online', 'game-store/cards/CardGameRules.md'),
  CardGameDefinition('blackjack', 'Blackjack', 'solo+online', 'game-store/cards/CardGameRules.md'),
  CardGameDefinition('klondike', 'Klondike Solitaire', 'solo', 'game-store/cards/CardGameRules.md'),
  CardGameDefinition('freecell', 'FreeCell', 'solo', 'game-store/cards/CardGameRules.md'),
  CardGameDefinition('hearts', 'Hearts', 'solo+online', 'game-store/cards/CardGameRules.md'),
  CardGameDefinition('spades', 'Spades', 'solo+online', 'game-store/cards/CardGameRules.md'),
  CardGameDefinition('crazy_eights', 'Crazy Eights', 'solo+online', 'game-store/cards/CardGameRules.md'),
  CardGameDefinition('war', 'War', 'solo+online', 'game-store/cards/CardGameRules.md'),
  CardGameDefinition('go_fish', 'Go Fish', 'solo+online', 'game-store/cards/CardGameRules.md'),
  CardGameDefinition('gin_rummy', 'Gin Rummy', 'solo+online', 'game-store/cards/CardGameRules.md'),
  CardGameDefinition('cribbage', 'Cribbage', 'solo+online', 'game-store/cards/CardGameRules.md'),
  CardGameDefinition('baccarat', 'Baccarat', 'solo+online', 'game-store/cards/CardGameRules.md'),
  CardGameDefinition('euchre', 'Euchre', 'solo+online', 'game-store/cards/CardGameRules.md'),
  CardGameDefinition('canasta', 'Canasta', 'solo+online', 'game-store/cards/CardGameRules.md'),
  CardGameDefinition('pinochle', 'Pinochle', 'solo+online', 'game-store/cards/CardGameRules.md'),
  CardGameDefinition('old_maid', 'Old Maid', 'solo+online', 'game-store/cards/CardGameRules.md'),
];
