import 'package:flutter/material.dart';

/// Resolves the optional CC0/public-domain deck downloaded by fetch_card_art.*.
/// PNG is used for Flutter runtime compatibility; SVG remains available in the cache.
class CardArt {
  static const root = 'assets/art/cc0-public-domain-deck';
  static String _rankName(String rank) => switch (rank) {
    'A' => 'ace', 'J' => 'jack', 'Q' => 'queen', 'K' => 'king', _ => rank,
  };
  static String _suitName(String suit) => suit.toLowerCase();
  static String assetPath({required String rank, required String suit}) =>
      '$root/png cards/card fronts/${_suitName(suit)}/${_rankName(rank)} of ${_suitName(suit)}.png';
  static Widget card({required String rank, required String suit, double width = 62}) => SizedBox(
    width: width, child: Image.asset(assetPath(rank: rank, suit: suit), fit: BoxFit.contain,
      errorBuilder: (_, __, ___) => _fallback(rank, suit)));
  static Widget _fallback(String rank, String suit) => Container(
    height: 88, alignment: Alignment.center,
    decoration: BoxDecoration(color: Colors.white, borderRadius: BorderRadius.circular(9)),
    child: Text('$rank${_symbol(suit)}', style: TextStyle(
      color: (suit == 'hearts' || suit == 'diamonds') ? Colors.red : Colors.black,
      fontSize: 20, fontWeight: FontWeight.bold)));
  static String _symbol(String suit) => switch (suit) {
    'clubs' => '♣', 'diamonds' => '♦', 'hearts' => '♥', 'spades' => '♠', _ => '?'
  };
}
