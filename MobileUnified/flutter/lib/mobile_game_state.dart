class MobileGameState {
  final String mode;
  final int cash;
  final int level;
  final int score;
  final bool bizVirtual;
  final String network;

  const MobileGameState({
    this.mode = 'default',
    this.cash = 10000,
    this.level = 1,
    this.score = 0,
    this.bizVirtual = true,
    this.network = 'offline',
  });
}

class MobileGameEngine {
  static MobileGameState start({String mode = 'default', int cash = 10000}) =>
      MobileGameState(mode: mode, cash: cash);
}
