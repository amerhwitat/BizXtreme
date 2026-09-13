import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "engine" / "python"))

from unified_engine import GameState


def test_tick_updates_score_and_cash():
    state = GameState(cash=10000)
    state.tick(revenue=250, cost=50)
    assert state.cash == 10200
    assert state.score == 200
    assert state.turn == 1


def test_snapshot_exposes_shared_state_contract():
    state = GameState(cash=500)
    snapshot = state.snapshot()
    assert snapshot["player"]["cash"] == 500
    assert snapshot["turn"] == 0
    assert snapshot["economy"]["coins"]["BIZ"] == 0.0
