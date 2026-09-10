"""Single Python entry point for starting the BizXtreme game/application."""

from .api import BizXtremeApi


def main() -> int:
    api = BizXtremeApi()
    print("BizXtreme game starting")
    print(api.health())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
