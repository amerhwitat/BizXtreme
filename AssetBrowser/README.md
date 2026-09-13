# In-Game Free Asset Browser

Unified GUI for browsing openly licensed game assets, reviewing provenance/licensing, downloading selected assets, and importing them into the BizXtreme `game_assets/` workspace.

Providers include Openverse for openly licensed images/audio, Poly Haven for CC0 3D/HDRI/textures, and a curated Kenney official catalog. Downloads are restricted to HTTPS provider hosts; archives are never executed. Each import records source, license, attribution metadata, SHA-256 and timestamp in `game_assets/manifest.json`.

Run with `scripts/run.bat`, `scripts/run.ps1`, or `scripts/run.sh`. Default GUI: `http://127.0.0.1:8790`.

Set `ASSET_BROWSER_PORT` or `ASSET_BROWSER_DIR` to customize runtime settings.
