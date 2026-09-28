#!/usr/bin/env python3
"""Structural validation for retro media containers."""
from pathlib import Path
import json, sys

root = Path(__file__).resolve().parents[2]
media = root / "retro" / "media"
errors = []
checked = []

def require(cond, message):
    if not cond:
        raise ValueError(message)

for path in sorted(media.rglob("*")):
    if not path.is_file():
        continue
    data = path.read_bytes()
    suffix = path.suffix.lower()
    try:
        if suffix == ".atr":
            require(len(data) >= 16 and data[:2] == bytes((0x96, 0x02)), "invalid ATR header")
        elif suffix == ".2mg":
            require(len(data) >= 64 and data[:4] == b"2IMG", "invalid 2MG header")
        elif suffix == ".dsk":
            require(len(data) >= 256 and (data[:8] in (b"MV - CPC", b"EXTENDED")), "invalid DSK header")
        elif suffix == ".adf":
            require(len(data) == 901120, "unexpected ADF size")
        elif suffix == ".tap":
            off = 0
            while off < len(data):
                require(off + 2 <= len(data), "truncated TAP length")
                size = int.from_bytes(data[off:off+2], "little")
                off += 2
                require(off + size <= len(data), "truncated TAP block")
                off += size
        elif suffix == ".st":
            require(len(data) >= 512, "ST image smaller than one sector")
        else:
            continue
        checked.append(str(path.relative_to(media)))
    except ValueError as exc:
        errors.append(f"{path.relative_to(media)}: {exc}")

report = {"checked": checked, "errors": errors, "emulator_execution": "pending", "certified": False}
(media / "structural-validation.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
print(json.dumps(report, indent=2))
sys.exit(1 if errors else 0)
