"""Shared, dependency-light BizXtreme game state and economy engine."""

from dataclasses import dataclass, field


@dataclass
class Economy:
    cash: float = 10000.0

    def transact(self, revenue: float = 0.0, cost: float = 0.0) -> None:
        self.cash += float(revenue) - float(cost)


@dataclass
class VirtualLedger:
    """In-game asset ledger; it never handles private keys or real settlement."""

    balances: dict[str, float] = field(default_factory=dict)

    def mint(self, symbol: str, amount: float) -> None:
        if amount < 0:
            raise ValueError("amount must be non-negative")
        self.balances[symbol] = self.balances.get(symbol, 0.0) + float(amount)


@dataclass
class GameState:
    cash: float = 10000.0
    score: int = 0
    turn: int = 0
    level: int = 1
    coins: dict[str, float] = field(default_factory=lambda: {"BIZ": 0.0})

    def tick(self, revenue: float = 0.0, cost: float = 0.0) -> None:
        """Advance one economic turn and apply net cash/score change."""
        net = float(revenue) - float(cost)
        self.cash += net
        self.score += int(net)
        self.turn += 1
        self.level = max(1, 1 + self.score // 10000)

    def snapshot(self) -> dict:
        return {
            "player": {
                "cash": self.cash,
                "level": self.level,
                "score": self.score,
            },
            "turn": self.turn,
            "economy": {"coins": dict(self.coins)},
        }
