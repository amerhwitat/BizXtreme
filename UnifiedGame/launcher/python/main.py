#!/usr/bin/env python3
import argparse, json, time

COINS = {"BIZ": {"name": "BizX Coin", "symbol": "BIZ", "virtual": True}}

def run(mode: str, cash: float):
    state = {
        "application": "BizXtreme Unified Game",
        "mode": mode,
        "runtime": "python",
        "player": {"cash": cash, "level": 1, "score": 0},
        "economy": {"coins": COINS},
        "rendering": {"requested": "auto", "available": ["terminal"]},
        "networking": {"mode": "offline", "status": "ready"},
        "status": "started",
    }
    print(json.dumps(state, indent=2))
    if mode == "tycoon":
        print("Tycoon session ready. Use the game runtime adapters for interactive rendering.")
    return state

def main():
    p = argparse.ArgumentParser(description="BizXtreme Unified Game")
    p.add_argument("--mode", choices=["default", "tycoon", "sandbox", "multiplayer"], default="default")
    p.add_argument("--cash", type=float, default=10000)
    args = p.parse_args()
    run(args.mode, args.cash)

if __name__ == "__main__":
    main()
