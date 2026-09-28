# Retro emulator build matrix

This repository contains orchestration metadata for building the open-source
retrocomputer emulator stack. Upstream emulator source remains under its
respective project license; it is not copied or relicensed by this file.

Targets:
- Commodore: VICE
- Atari 8-bit: Atari800
- Apple II: AppleWin
- ZX Spectrum: Fuse/libspectrum
- Amstrad CPC: Caprice32
- MSX: openMSX
- BBC Micro: B-em
- Amiga: FS-UAE
- Atari ST: Hatari

The build system must pin an upstream tag/commit, verify the source archive,
build on Windows/Linux/macOS where supported, and publish artifacts only after
the target-specific smoke test succeeds.

Proprietary ROMs are intentionally excluded. Users must provide ROMs they are
legally entitled to use.
