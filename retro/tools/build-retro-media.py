#!/usr/bin/env python3
"""Deterministic retro-media builder.

Creates a conservative C64 PRG/D64 test image and packages any existing
retro/media files.  It intentionally does not embed proprietary ROMs.
"""
from pathlib import Path
import hashlib, json, zipfile

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/"retro"/"media"
OUT.mkdir(parents=True,exist_ok=True)

# C64 BASIC V2: 10 PRINT "BIZX RETRO DEMO":20 GOTO 10
body1=bytes([0x99,0x20,0x22])+b"BIZX RETRO DEMO"+bytes([0x22,0])
body2=bytes([0x89,0x20,0x31,0x30,0])
addr=0x0801
prg=bytearray([addr&255,addr>>8])
for line,body in [(10,body1),(20,body2)]:
    nxt=addr+4+len(body)
    prg += bytes([nxt&255,nxt>>8,line&255,line>>8])+body
    addr=nxt
prg += b"\0\0"
(OUT/"BizX-C64.prg").write_bytes(prg)

# Standard 35-track C64 D64 geometry.
sectors=[21]*17+[19]*7+[18]*6+[17]*5
offset={}
p=0
for t,n in enumerate(sectors,1):
    for s in range(n):
        offset[(t,s)]=p;p+=256
d=bytearray(p)
bam=offset[(18,0)]
d[bam:bam+4]=bytes([18,1,0x41,0])
for t,n in enumerate(sectors,1):
    base=bam+4+(t-1)*4
    free=n
    bits=bytearray(3)
    for s in range(n): bits[s//8]|=1<<(s%8)
    d[base]=free; d[base+1:base+4]=bits
# directory track/sector
for t,s in [(18,0),(18,1)]:
    base=bam+4+(t-1)*4
    d[base]=max(0,d[base]-1); d[base+1+s//8]&=~(1<<(s%8))
db=offset[(18,1)]
d[db]=0; d[db+1]=0
# store PRG in track 17 sector 0
o=offset[(17,0)]
d[o]=0; d[o+1]=len(prg)+1
d[o+2:o+2+len(prg)]=prg
# directory entry
e=db+2; d[e]=0x82; d[e+1:e+17]=b"BIZX".ljust(16,b"\xa0")
d[e+0x11]=17; d[e+0x12]=0
d[e+0x1c]=1
# mark data sector used
base=bam+4+(17-1)*4
d[base]=max(0,d[base]-1); d[base+1]&=~1
(OUT/"BizX-C64.d64").write_bytes(d)

manifest={"format_version":1,"generated_by":"retro/tools/build-retro-media.py",
"files":[],"rom_policy":"No proprietary ROMs are included."}
for f in sorted(OUT.iterdir()):
    if f.is_file():
        manifest["files"].append({"name":f.name,"bytes":f.stat().st_size,
                                  "sha256":hashlib.sha256(f.read_bytes()).hexdigest()})
(OUT/"retro-media-manifest.json").write_text(json.dumps(manifest,indent=2)+"\n")
with (OUT/"SHA256SUMS.txt").open("w") as h:
    for f in sorted(OUT.iterdir()):
        if f.name=="SHA256SUMS.txt": continue
        h.write(hashlib.sha256(f.read_bytes()).hexdigest()+"  "+f.name+"\n")
zipfile_path=ROOT/"retro"/"dist"/"retro-media.zip"
zipfile_path.parent.mkdir(parents=True,exist_ok=True)
with zipfile.ZipFile(zipfile_path,"w",zipfile.ZIP_DEFLATED) as z:
    for f in sorted(OUT.iterdir()):
        if f.is_file(): z.write(f,f.name)
print(zipfile_path)
