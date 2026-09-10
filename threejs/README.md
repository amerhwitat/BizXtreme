# BizXtreme Three.js Edition

Browser-first companion implementation of **BizXtreme: The Living Frontier**. It preserves the original game concept and shares the story, events, starter pack and marketplace vocabulary with the Unity edition.

## Stack

- Three.js for 3D rendering
- Vite for local development/build
- ES modules
- WebGL as the baseline renderer, with a future WebGPU path

Three.js officially documents WebGL capability detection and also provides WebGPU capability detection. The project therefore keeps WebGL as the compatibility baseline while leaving WebGPU as an enhancement path. See the official documentation: https://threejs.org/docs/pages/WebGL.html and https://threejs.org/docs/pages/WebGPU.html.

## Run

```bash
npm install
npm run dev
```

## Build

```bash
npm run build
```

## Current scope

The first implementation provides the professional game menu, 3D frontier scene, story chapters, events, starter inventory and marketplace vocabulary. Wallet signing and blockchain operations should remain behind the existing secure provider/adapter boundary; this browser client must never receive server-generated private keys or seed phrases.

The Three.js scene follows the standard scene/camera/renderer/animation-loop architecture described in the official manual.
