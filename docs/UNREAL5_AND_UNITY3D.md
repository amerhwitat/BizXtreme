# BizXtreme Unreal 5 / Unity 3D interoperability

BizXtreme now includes an engine-neutral 3D asset boundary and a Unity C# integration package. The repository keeps the Unity implementation in C# as requested by the language-separated architecture.

## Unity

Use `Unity3D/package.json` as a local UPM package or copy `Unity3D/Assets/` into a project. The editor `AssetPostprocessor` applies deterministic import defaults for FBX/OBJ/glTF assets. Unity documents `AssetPostprocessor` as an extension point around asset import, and Unity supports both `.unitypackage` and UPM package distribution.

References:
- https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetPostprocessor.html
- https://docs.unity.com/en-us/asset-store/publishing/introduction

## Unreal 5 interoperability

BizXtreme portable assets are deliberately engine-neutral so they can be imported into Unreal 5 using the engine's FBX/glTF/Datasmith pipelines. When a native Unreal C++ integration is required, the canonical C++ implementation remains in BizX's `Unreal5/BizXUnreal/` boundary so that BizX and BizXtreme do not duplicate the native module unnecessarily.

References:
- https://dev.epicgames.com/documentation/en-us/unreal-engine/fbx-content-pipeline
- https://dev.epicgames.com/documentation/en-us/unreal-engine/importing-datasmith-content-into-unreal-engine
- https://dev.epicgames.com/documentation/en-us/unreal-engine/datasmith-supported-software-and-file-types

## Assets

`3D/assets/bizxtreme_demo.obj` is a small original demonstration mesh. OBJ is used as a source-control-friendly interchange example; production projects may use FBX, glTF/glb, USD or Datasmith according to their target-engine pipeline and licensing requirements.

## Coordinate and unit policy

The integration model stores transforms explicitly. Engine adapters must document unit and coordinate conversion instead of silently assuming identical conventions. Unreal's documented world unit is centimeters; Unity projects commonly use meters. Conversion belongs at the engine boundary.
