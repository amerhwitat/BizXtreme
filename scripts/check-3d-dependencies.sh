#!/usr/bin/env bash
set -u
command -v git >/dev/null && echo 'OK git' || echo 'WARN missing git'
command -v dotnet >/dev/null && echo 'OK dotnet' || echo 'WARN missing dotnet'
if [[ -n "${UNITY_EDITOR_PATH:-}" ]]; then echo "Unity editor: $UNITY_EDITOR_PATH"; else echo 'Unity: set UNITY_EDITOR_PATH before automated builds'; fi
if [[ -n "${UNREAL_ENGINE_ROOT:-}" ]]; then echo "UE5 root: $UNREAL_ENGINE_ROOT"; else echo 'UE5 native plugin is maintained in BizX'; fi
