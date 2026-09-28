# Retro media matrix

BizX, BizXtreme and NLP share a common retro-media build policy.

## Targets
C64, C128, VIC-20, Plus/4, PET, Atari 8-bit, Apple II, ZX Spectrum, Amstrad CPC, MSX, BBC Micro, TRS-80, Amiga 500 and Atari ST.

## Artifact policy
Media generators create deterministic containers and checksums. A structurally valid image is **not** treated as a bootable/native port. Emulator smoke tests must pass before an artifact is called certified.

## ROM policy
No proprietary ROM/Kickstart images are redistributed. Users supply legally obtained firmware required by their emulator.

## Build
Run: `python3 retro/tools/build-retro-media.py`

The GitHub Actions workflow packages generated media as an artifact. Version tags can publish the ZIP as a release asset.

## Emulator matrix
See `retro/EMULATOR-MATRIX.json` and `retro/EMULATOR-BUILD.md`.
