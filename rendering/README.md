# BizXtreme real-time rendering layer

BizXtreme exposes a common scene/asset contract to multiple open-source rendering and game-engine ecosystems.

## Engine targets

- Unity 3D / C#
- Godot 4
- Three.js/WebGL/WebGPU
- Bevy/Rust
- OGRE/C++
- bgfx/C++
- Filament/C++

The Unity implementation remains the primary C# engine integration. Other engines are optional adapters and are not vendored.

## Real-time capabilities

The renderer contract covers:

- PBR materials
- HDR lighting
- image-based lighting
- directional/point/spot lights
- shadow maps
- skeletal/static meshes
- glTF/GLB scene import
- OBJ/FBX conversion boundaries
- 2D textures/sprites
- cameras and post-processing capability discovery
- Vulkan/Direct3D/Metal/OpenGL/WebGL/WebGPU capability reporting

## Free/public asset import

The asset browser/import layer is designed to import only assets whose current metadata/license explicitly permits downloading and reuse. Preferred providers include CC0/public-domain sources such as Poly Haven and Smithsonian Open Access. Other repositories are imported only when their specific asset license permits it.

Poly Haven states that its models, textures and HDRIs are CC0 and its API is available for commercial use. Smithsonian Open Access provides CC0 2D/3D assets and documents glTF/glb/OBJ access formats.

References:
- https://polyhaven.com/license
- https://polyhaven.com/our-api
- https://www.si.edu/openaccess/faq
- https://3d.si.edu/collections/openaccesshighlights
- https://docs.godotengine.org/en/latest/tutorials/rendering/renderers.html
- https://bevy.org/
- https://www.ogre3d.org/
- https://github.com/bkaradzic/bgfx
- https://github.com/google/filament
