#!/usr/bin/env python3
import argparse
import json
import sys
from pathlib import Path

ENGINE = Path(__file__).resolve().parents[2] / "engine" / "python"
if str(ENGINE) not in sys.path:
    sys.path.insert(0, str(ENGINE))

from unified_engine import GameState

COINS = {"BIZ": {"name": "BizX Coin", "symbol": "BIZ", "virtual": True}}


def run(mode: str, cash: float):
    state = GameState(cash=cash)
    snapshot = state.snapshot()
    snapshot["application"] = "BizXtreme Unified Game"
    snapshot["mode"] = mode
    snapshot["runtime"] = "python"
    snapshot["economy"]["coin_metadata"] = COINS
    snapshot["rendering"] = {"requested": "auto", "available": ["terminal"]}
    snapshot["networking"] = {"mode": "offline", "status": "ready"}
    snapshot["status"] = "started"
    print(json.dumps(snapshot, indent=2))
    if mode == "tycoon":
        print("Tycoon session ready. Shared economy state is active; use runtime adapters for interactive rendering.")
    return snapshot


def main():
    p = argparse.ArgumentParser(description="BizXtreme Unified Game")
    p.add_argument("--mode", choices=["default", "tycoon", "sandbox", "multiplayer"], default="default")
    p.add_argument("--cash", type=float, default=10000)
    args = p.parse_args()
    run(args.mode, args.cash)


if __name__ == "__main__":
    main()
