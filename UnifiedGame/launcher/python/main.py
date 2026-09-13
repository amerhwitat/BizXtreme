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
ASSET_BROWSER = "http://127.0.0.1:8790"


def run(mode: str, cash: float):
    state = GameState(cash=cash)
    snapshot = state.snapshot()
    snapshot["application"] = "BizXtreme Unified Game"
    snapshot["mode"] = mode
    snapshot["runtime"] = "python"
    snapshot["economy"]["coin_metadata"] = COINS
    snapshot["rendering"] = {"requested": "auto", "available": ["terminal"]}
    snapshot["networking"] = {"mode": "offline", "status": "ready"}
    snapshot["asset_browser"] = {
        "enabled": True,
        "url": ASSET_BROWSER,
        "providers": ["Openverse", "Poly Haven", "Kenney"],
        "import_directory": "game_assets/",
        "provenance_manifest": "game_assets/manifest.json",
    }
    snapshot["status"] = "started"
    print(json.dumps(snapshot, indent=2))
    if mode == "tycoon":
        print("Tycoon session ready. Use the in-game Asset Browser at http://127.0.0.1:8790 to browse and import licensed assets.")
    return snapshot


def main():
    p = argparse.ArgumentParser(description="BizXtreme Unified Game")
    p.add_argument("--mode", choices=["default", "tycoon", "sandbox", "multiplayer"], default="default")
    p.add_argument("--cash", type=float, default=10000)
    args = p.parse_args()
    run(args.mode, args.cash)


if __name__ == "__main__":
    main()
