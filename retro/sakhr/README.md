# Sakhr AX-170 / AX-230

This directory integrates the Arabic Sakhr MSX1 targets into the BizX/BizXtreme/NLP retro stack.

## Targets

- AX-170: MSX1, Z80A, 64 KB RAM, 16 KB VRAM, two cartridge slots.
- AX-230: MSX1, Z80A, 64 KB RAM, 16 KB VRAM, one cartridge slot.

The target emulators are MAME and openMSX. MAME exposes the machines as \`ax170\` and \`ax230\`.

## Project cartridge images

Run:

    python3 retro/tools/build-sakhr-msx-images.py

The builder produces 32 KB MSX cartridge images for BizX, BizXtreme and nlp for both Sakhr models, plus SHA-256 metadata.

## Firmware policy

Sakhr machine firmware/BIOS dumps are not included or redistributed. Use legally obtained firmware where an emulator configuration requires it. The generated cartridge images contain only project-generated code/data.

## Certification

Image generation and structural validation are separate from emulator certification. A target is marked emulator-certified only after an actual MAME/openMSX smoke test has executed the corresponding image.
