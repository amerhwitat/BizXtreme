"""Single Python entry point for starting BizXtreme and Tycoon mode."""

from .api import BizXtremeApi
from .game.tycoon import TycoonGame


def main(mode: str = "default") -> int:
    api = BizXtremeApi()
    print("BizXtreme game starting")
    print(api.health())
    if mode.lower() == "tycoon":
        game = TycoonGame(cash=10_000)
        print(f"BizXtreme Tycoon ready: cash={game.cash}")
    return 0


if __name__ == "__main__":
    import sys
    raise SystemExit(main(sys.argv[1] if len(sys.argv) > 1 else "default"))
