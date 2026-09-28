#!/usr/bin/env python3
"""Build and package retro media already produced by the target-specific builders.

This script deliberately does not manufacture bootable ports. It discovers
media under retro/media, records size/SHA-256, and creates a reproducible ZIP.
"""
from pathlib import Path
import hashlib, json, zipfile

ROOT=Path(__file__).resolve().parents[2]
MEDIA=ROOT/"retro"/"media"
DIST=ROOT/"retro"/"dist"
MEDIA.mkdir(parents=True, exist_ok=True)
DIST.mkdir(parents=True, exist_ok=True)

allowed={".d64",".d71",".d81",".prg",".tap",".t64",".atr",".2mg",".dsk",".ssd",".dsd",".adf",".st",".img"}
items=[]
for p in sorted(MEDIA.rglob("*")):
    if p.is_file() and p.suffix.lower() in allowed:
        data=p.read_bytes()
        items.append({"name":str(p.relative_to(MEDIA)).replace("\\","/"),
                      "bytes":len(data),
                      "sha256":hashlib.sha256(data).hexdigest()})

manifest={
  "schema_version":1,
  "project":"BizX Retro Media",
  "status":"discovered-and-packaged",
  "artifacts":items,
  "verification":{"structural":"sha256-recorded","emulator_execution":"pending per target"},
  "rom_policy":"No proprietary ROM images are redistributed."
}
(MEDIA/"retro-media-manifest.json").write_text(json.dumps(manifest,indent=2)+"\n",encoding="utf-8")
with (MEDIA/"SHA256SUMS.txt").open("w",encoding="utf-8") as f:
    for x in items: f.write(f'{x["sha256"]}  {x["name"]}\n')

out=DIST/"retro-media.zip"
with zipfile.ZipFile(out,"w",zipfile.ZIP_DEFLATED) as z:
    for p in sorted(MEDIA.rglob("*")):
        if p.is_file() and (p.suffix.lower() in allowed or p.name in {"retro-media-manifest.json","SHA256SUMS.txt"}):
            z.write(p,p.relative_to(MEDIA).as_posix())
print(f"Packaged {len(items)} media files -> {out}")
