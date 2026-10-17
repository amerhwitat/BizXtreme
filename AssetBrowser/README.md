# In-Game Free Asset Browser

Unified GUI for browsing openly licensed game assets, reviewing provenance/licensing, downloading selected assets, and importing them into the BizXtreme `game_assets/` workspace.

Providers include Openverse for openly licensed images/audio, Poly Haven for CC0 3D/HDRI/textures, and a curated Kenney official catalog. Downloads are restricted to HTTPS provider hosts; archives are never executed. Each import records source, license, attribution metadata, SHA-256 and timestamp in `game_assets/manifest.json`.

Run with `scripts/run.bat`, `scripts/run.ps1`, or `scripts/run.sh`. Default GUI: `http://127.0.0.1:8790`.

Set `ASSET_BROWSER_PORT` or `ASSET_BROWSER_DIR` to customize runtime settings.


## Browser GUI and local API

Run `python3 AssetBrowser/python/app.py` from the repository root (or set `ASSET_BROWSER_PORT`) to start the local service. The web GUI supports provider search, license/source review, installed-manifest inspection, and importing supported files into the local asset store. It validates provider download hosts and file extensions before importing.

The service no longer sends wildcard CORS headers. To connect the published portfolio GUI, explicitly configure the exact origin:

```bash
ASSET_BROWSER_CORS_ORIGINS=https://amerhwitat.github.io python3 AssetBrowser/python/app.py
```

By default, only local development origins are allowed. Do not use a wildcard origin. The portfolio GUI does not itself download assets or execute Python; the local service performs imports after the user confirms. Review provider license metadata before shipping an asset.
