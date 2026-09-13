"""Shared, dependency-light BizXtreme game state engine."""

from dataclasses import dataclass, field


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
