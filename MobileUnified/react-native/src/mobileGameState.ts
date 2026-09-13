export type MobileGameState = {
  mode: string;
  cash: number;
  level: number;
  score: number;
  bizVirtual: boolean;
  network: 'offline' | 'online';
};

export const startMobileGame = (mode = 'default', cash = 10000): MobileGameState => ({
  mode,
  cash,
  level: 1,
  score: 0,
  bizVirtual: true,
  network: 'offline',
});
