# Public asset providers

The importer must preserve source URL, asset identifier, license, attribution, retrieval timestamp and SHA-256. It must not treat a search result as permission to download or redistribute an asset.

## Preferred open/public sources

- Poly Haven — CC0 models, textures and HDRIs; public API.
- Smithsonian Open Access — CC0-designated 2D/3D collection items, including glTF/glb/OBJ.
- NASA 3D resources — use only assets whose individual NASA media terms permit the intended reuse.

The importer should expose a license gate and default to **deny** when license information is missing or ambiguous.

References:
- https://polyhaven.com/license
- https://polyhaven.com/our-api
- https://www.si.edu/openaccess/faq
- https://3d.si.edu/collections/openaccesshighlights
- https://nasa3d.arc.nasa.gov/
