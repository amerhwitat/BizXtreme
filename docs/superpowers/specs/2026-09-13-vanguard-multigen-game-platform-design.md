# BizXtreme Vanguard Multi-Genre Game Platform — Design Specification

**Date:** 2026-09-13  
**Status:** Approved design expansion; implementation follows the repository's Superpowers plan/TDD gates.

## Objective
Extend BizXtreme into an original cross-platform game platform spanning AAA-style FPS, RTS/strategy, tactical, 4X, tower-defense, action, co-op and mobile experiences. Share deterministic simulation contracts, multiplayer protocols, asset provenance, renderer-neutral scene data, AI interfaces, audio/VFX metadata, and language bindings.

The project uses genre-level inspiration from successful games and open-source projects without copying proprietary characters, maps, dialogue, brands, source code, cinematics, UI artwork, sounds, music, or other protected content.

## Game families
- Vanguard FPS: tactical first-person combat, campaign/co-op, competitive multiplayer, battle royale/extraction variants, vehicles, drones, squad commands, dynamic environments, replay/spectator.
- Vanguard Strategy: classic base-building RTS, modern combined-arms RTS, 3D tactical RTS, 4X/grand-strategy, tower defense, commander/hero layer, naval/air/space, economy/logistics, FPS↔RTS hybrid.
- Shared action/mobile: top-down action, twin-stick/shooter, survival/extraction, lightweight 2D/3D, touch-first and controller support.

## Research inputs
Research targets include OpenRA, 0 A.D., Warzone 2100, Bevy, O3DE, Defold, Kenney, Quaternius, OpenGameArt and other openly documented ecosystems. Their architecture and genre patterns are research input only.

Warzone 2100 demonstrates open-source 3D RTS, online/LAN multiplayer, AI bots, extensive technology, customizable units and multiple graphics backends. OpenRA demonstrates modern RTS controls, fog of war, veterancy, replay/observer support, multiplayer and modding. O3DE provides an Apache-2.0 high-fidelity real-time engine. Defold provides lightweight cross-platform mobile/web/desktop deployment. Bevy provides a parallel ECS/render-graph model in Rust.

## Rendering architecture
A renderer-neutral contract feeds adapters for Unreal Engine C++, Unity C#, native C++ Vulkan/OpenGL/Direct3D, WebGPU/Three.js, Godot, O3DE, Bevy/Rust, Defold/Lua, Swift/Metal, Kotlin/Android and Flutter/Impeller. High-fidelity rendering is owned by appropriate native engines; other languages provide services, mobile clients, servers, AI, tooling, content processing or adapters.

## VFX
Shared VFX schema: particles, smoke/fire/explosions, muzzle flashes, tracers, debris, weather, volumetric fog, dust/sand/snow/rain, water/terrain effects, decals, destruction, post-processing, screen-space effects, lighting, day/night, GPU particles, LOD and mobile fallback tiers. Profiles: ultra/high/medium/low/mobile.

## Audio and voice
Audio metadata covers weapons, impacts, vehicles, explosions, UI, environment, footsteps, ambience, music, radio/comms, commander voices, NPC dialogue, dynamic mixing, spatial/3D audio and mobile compression. Voice content is original or properly licensed; generated voice is used only under applicable terms.

## Asset provenance
Use only assets whose licenses permit intended use. Prefer CC0/public-domain and compatible licenses. Every imported asset gets source URL, author, license, license URL, acquisition date, SHA-256, modification status, attribution requirements and redistribution restrictions. Do not import proprietary commercial-game assets merely because they are downloadable.

## Strategy simulation
Entities: player, commander, squad, unit, building, resource node, production queue, technology, ability, projectile, vehicle, aircraft, ship, territory, objective, faction, diplomacy relation, logistics route, fog-of-war cell.

Requirements: deterministic ticks, deterministic numeric policy, pathfinding, formations, line of sight, cover, economy, production, research, construction, damage/repair, supply/logistics, objectives and replay serialization.

## FPS/RTS bridge
A shared battlefield state can be observed from strategic or first-person views. Commanders issue orders while players can enter soldiers or vehicles. The authoritative simulation remains the source of truth.

## Multiplayer
Support local/LAN, dedicated server, client/server, host/listen server, P2P, hybrid/relay, cooperative, competitive, team play, spectator, replay and matchmaking/lobbies.

Protocol areas: authentication/session identity, lobby discovery, party/squad state, command replication, snapshot/delta replication, prediction/reconciliation, authoritative damage/state, RTS orders, FPS movement/combat, inventory, vehicles, AI state, objectives, chat/voice metadata, reconnect, safe host migration and replay capture. Clients are untrusted and competitive outcomes are server-validated.

## RNN/LLM integration
RNN services: player sequence prediction, unit movement prediction, threat forecasting, resource-flow forecasting, tactical formation prediction, anomaly detection and network telemetry prediction. LLM services: commander assistant, mission briefings, strategy explanation, natural-language tactical orders, replay analysis, NPC dialogue, dynamic objective authoring and narrative assistance. AI output is advisory and cannot directly override authoritative simulation.

## Mobile
Use shared contracts with touch controls, virtual joystick/action layouts, adaptive UI, 30/60 FPS profiles, thermal/battery budgets, asset streaming, compressed textures/audio, low-memory scene variants, offline campaign/skirmish where practical, reconnect-aware multiplayer and Android/iOS services. Defold, Unity, Godot, native Kotlin/Swift and Flutter are used according to workload.

## Repository layout
```text
game-store/vanguard/
strategy/
rendering/strategy/
multiplayer/strategy/
neural/strategy/
audio/strategy/
vfx/strategy/
assets/strategy/
tools/strategy/
tests/strategy/
```
Language implementations follow existing C++, desktop, Unreal5, Unity3D, Node.js, Java, Python, JavaScript, TypeScript, Apple/Swift, Kotlin, Flutter, web and related repository trees.

## Testing
Cover deterministic simulation, serialization, pathfinding, economy, combat, networking, reconnect, replay determinism, asset-manifest validation, audio/VFX-manifest validation, renderer smoke tests and mobile budget profiles.

## Security/IP
Never ship proprietary game assets without rights. Preserve license notices. Treat network clients as untrusted. Keep wallet secrets out of gameplay/network/save data. Keep AI advisory and sandboxed. Validate multiplayer commands server-side.

## Acceptance criteria
Both BizX and BizXtreme must contain synchronized contracts/documentation, runnable reference implementations for supported runtimes, multiplayer protocol definitions, original strategy/FPS storyboards, asset provenance manifests, VFX/audio/voice schemas, tests and CI validation. Build-success claims require actual verification evidence.
