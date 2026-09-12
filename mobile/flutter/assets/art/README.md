# Card artwork cache

BizXtreme uses a license-verified external art cache rather than generated artwork for the card games.

Run one of:

- `../scripts/fetch_card_art.ps1` on Windows PowerShell
- `../scripts/fetch_card_art.bat` on Windows CMD
- `../scripts/fetch_card_art.sh` on Linux/macOS

The primary source is the OpenDecks Public Domain / CC0 Playing Cards repository. The fetcher copies its SVG and PNG deck into `cc0-public-domain-deck/` and preserves the source license/readme.

The Flutter UI has a programmatic card fallback, so a fresh checkout remains functional before the optional asset cache is downloaded.
