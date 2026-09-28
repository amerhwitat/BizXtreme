#!/usr/bin/env python3
from pathlib import Path
import hashlib, json
ROOT=Path(__file__).resolve().parents[2]
DIST=ROOT/"retro"/"dist"/"sakhr-msx"
DIST.mkdir(parents=True,exist_ok=True)
PROJECTS=("BizX","BizXtreme","nlp")
MODELS=("AX-170","AX-230")
def make_rom(project,model):
    rom=bytearray([0xFF])*0x8000
    rom[0:2]=b"AB"
    rom[2:4]=(0x4010).to_bytes(2,"little")
    rom[8:10]=(0x4010).to_bytes(2,"little")
    rom[0x10:0x16]=bytes((0xF3,0x21,0x00,0x00,0x18,0xFE))
    label=f"{project} / Sakhr {model} / MSX1".encode("ascii")
    rom[0x100:0x100+len(label)]=label
    return bytes(rom)
items=[]
for project in PROJECTS:
    for model in MODELS:
        path=DIST/f"{project}-Sakhr-{model}.rom"
        path.write_bytes(make_rom(project,model))
        items.append({"name":path.name,"bytes":path.stat().st_size,"sha256":hashlib.sha256(path.read_bytes()).hexdigest()})
manifest={"schema_version":1,"target":"Sakhr MSX1","models":list(MODELS),"artifacts":items,"emulators":["MAME","openMSX"],"execution":"pending","firmware_policy":"Machine firmware is not redistributed."}
(DIST/"manifest.json").write_text(json.dumps(manifest,indent=2)+"\n")
with (DIST/"SHA256SUMS.txt").open("w") as f:
    for item in items: f.write(f'{item["sha256"]}  {item["name"]}\n')
print(json.dumps(manifest,indent=2))
