#if UNITY_EDITOR
using UnityEditor;
using UnityEngine;

namespace BizXtreme.Editor
{
    public sealed class BizXtremeModelPostprocessor : AssetPostprocessor
    {
        void OnPreprocessModel()
        {
            if (!assetPath.EndsWith(".fbx", System.StringComparison.OrdinalIgnoreCase) &&
                !assetPath.EndsWith(".obj", System.StringComparison.OrdinalIgnoreCase) &&
                !assetPath.EndsWith(".gltf", System.StringComparison.OrdinalIgnoreCase))
                return;

            var importer = (ModelImporter)assetImporter;
            importer.globalScale = 1.0f;
            importer.importBlendShapes = true;
            importer.importMaterials = true;
            importer.importAnimation = true;
        }
    }
}
#endif
