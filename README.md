# BizXtreme

BizXtreme is the extended BizX application/game repository, including WebGL/Three.js, Unity/C#, wallet, crypto, game, Aurora, Chimera integration and Kotlin mobile material.

## Source-code citation index

| Area | Source |
|---|---|
| Windows Visual C++ | [desktop/vcpp/](desktop/vcpp/) |
| Windows C# / WPF | [desktop/dotnet/](desktop/dotnet/) |
| Unity 3D C# package | [Unity3D/](Unity3D/) |
| Portable 3D assets | [3D/assets/](3D/assets/) |
| Node.js | [nodejs/](nodejs/) |
| Java | [java/](java/) |
| Python | [python/](python/) |
| JavaScript | [javascript/](javascript/) |
| TypeScript | [typescript/](typescript/) |
| Web | [web/](web/) |
| Three.js/WebGL | [threejs/](threejs/) |
| Existing Unity/C# | [Assets/](Assets/) |
| Kotlin mobile | [kotlin/mobile/](kotlin/mobile/) |
| Apple/Swift | [apple/](apple/) |
| Chimera integration | [chimera/](chimera/) |
| Aurora integration | [aurora_integration.json](aurora_integration.json) |
| Documentation | [docs/](docs/) |

## Language-separated implementations

- `desktop/vcpp/` — standalone native Visual C++ Windows desktop implementation.
- `desktop/dotnet/` — standalone C# WPF Windows desktop implementation.
- `Unity3D/` — Unity C# package and editor integration.
- `3D/assets/` — engine-neutral demonstration geometry.
- `nodejs/`, `java/`, `python/`, `javascript/`, `typescript/`, `web/`, `Assets/`, `threejs/` — runtime/application implementations.
- `docs/` — language-neutral architecture and integration documentation.

## Unreal Engine 5 / Unity 3D interoperability

BizXtreme's requested C# implementation is centered on Unity 3D under `Unity3D/`. It contains a UPM package manifest, runtime world-object model and an editor `AssetPostprocessor` that applies deterministic model-import defaults for FBX, OBJ and glTF assets.

Portable geometry is under `3D/assets/`. The included OBJ can be imported into Unity and Unreal-compatible DCC workflows. Unreal Engine 5 interoperability is intentionally engine-neutral in this repository; the native C++ UE5 plugin boundary is maintained in BizX's `Unreal5/BizXUnreal/` so the two repositories share one native module instead of duplicating C++ code.

See [`docs/UNREAL5_AND_UNITY3D.md`](docs/UNREAL5_AND_UNITY3D.md).

## Mobile communications

BizXtreme Mobile uses the shared conversation contract with BizX: conversation ID, sender ID, monotonic sequence and SHA-256 payload integrity. It provides microphone/speaker/camera capability detection and a WebRTC media boundary.

## Chimera 128D + authenticated P2P

BizXtreme participates in the shared Chimera multidimensional application fabric. The optional P2P layer is authenticated and opt-in and supports capability exchange, request/response, pub/sub, snapshot/delta synchronization, content-addressed state, sequence numbers and payload integrity.

## Licensing

New and modified BizXtreme code is intended for GNU GPL v3 or later. Third-party assets, Unity packages and engine SDKs retain their own licenses.

## External documentation citations

- Epic Games, Unreal Engine FBX Content Pipeline: https://dev.epicgames.com/documentation/en-us/unreal-engine/fbx-content-pipeline
- Epic Games, Datasmith Import: https://dev.epicgames.com/documentation/en-us/unreal-engine/importing-datasmith-content-into-unreal-engine
- Epic Games, Datasmith supported formats: https://dev.epicgames.com/documentation/en-us/unreal-engine/datasmith-supported-software-and-file-types
- Unity, Asset Store package formats: https://docs.unity.com/en-us/asset-store/publishing/introduction
- Unity, AssetPostprocessor: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetPostprocessor.html
