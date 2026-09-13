# BizXtreme Vanguard Multi-Genre Game Platform — Design Specification

**Date:** 2026-09-13  
**Status:** Approved design expansion; implementation follows repository Superpowers plan/TDD/verification gates.

## Objective
Extend BizXtreme into an original cross-platform game platform spanning AAA-style tactical FPS, RTS/strategy, tactical, 4X, tower-defense, action, co-op, voxel/sandbox and mobile experiences. Share deterministic simulation contracts, multiplayer protocols, asset provenance, renderer-neutral scene data, AI interfaces, audio/VFX metadata, and language bindings.

The project may use genre-level inspiration from competitive tactical FPS, Roblox-style creator sandboxes, Minecraft-style voxel survival/building, and open-source game engines/projects, but must not copy proprietary characters, maps, dialogue, brands, source code, cinematics, UI artwork, sounds, music, textures, meshes, animations, or other protected content.

## Game families
- Vanguard FPS: original competitive tactical first-person combat with attack/defend objectives, economy/loadout phases, round-based matches, campaign/co-op, competitive multiplayer, extraction/survival variants, vehicles where appropriate, drones, squad commands, dynamic environments, replay/spectator and training modes.
- Vanguard Strategy: classic base-building RTS, modern combined-arms RTS, 3D tactical RTS, 4X/grand-strategy, tower defense, commander/hero layer, naval/air/space, economy/logistics, FPS↔RTS hybrid.
- Vanguard Sandbox/Voxel: original creator-focused multiplayer worlds, block/voxel construction, procedural terrain, crafting, survival/creative modes, automation systems, scripting/mod APIs, avatars and UGC manifests.
- Shared action/mobile: top-down action, twin-stick/shooter, survival/extraction, lightweight 2D/3D, touch-first and controller support.

## Competitive tactical FPS design
The competitive FPS is an original IP with the high-level qualities of round-based tactical shooters: team objectives, asymmetric attack/defense roles, economy/loadout management, precise movement, recoil/weapon handling, utility deployment, map control, information gathering, audio cues, tactical communication, spectator/replay and competitive ranking. It must not reproduce Counter-Strike maps, weapons, models, names, sounds, UI, characters, logos or other Valve assets.

Core systems:
- first-person movement, sprint/crouch/prone where applicable, vault/lean, acceleration and movement states;
- authoritative hitscan/projectile simulation, recoil, spread, armor, damage zones and penetration policy;
- round state machine, warmup, buy/loadout phase, objective phase, round end and match transitions;
- team economy, rewards, inventory/loadout abstraction and configurable shop/catalog;
- original objective types with multiple win conditions;
- footsteps, occlusion-aware audio cues, environmental sound propagation and radio communication;
- tactical HUD, minimap, objective markers, teammate state and spectator overlays;
- replay/event timeline and deterministic match metadata;
- bot/training opponents and server-side anti-cheat validation hooks.

## Multiplayer architecture
All game families share a transport-independent multiplayer contract with these modes:
- dedicated authoritative client/server;
- listen/host server;
- LAN server discovery;
- direct peer-to-peer sessions for supported cooperative/private modes;
- hybrid P2P plus relay/dedicated authority;
- optional server migration for non-ranked sessions;
- matchmaking, parties, squads, lobbies and reconnect;
- spectator and replay sessions.

The competitive/ranked path is server-authoritative. P2P is an explicit mode with host trust limitations and must never silently replace authoritative competitive infrastructure.

Protocol layers:
1. identity/session and capability negotiation;
2. lobby/party/matchmaking;
3. reliable command channel;
4. unreliable high-frequency input/state channel;
5. snapshot/delta replication;
6. client prediction and reconciliation;
7. interpolation/extrapolation;
8. authoritative movement, combat, inventory and objective validation;
9. voice/chat metadata;
10. replay/event capture;
11. reconnect/resume and optional safe host migration;
12. telemetry, abuse/rate limiting and anti-cheat hooks.

Transport adapters should cover UDP, QUIC, WebSocket and WebRTC where suitable. IPv4/IPv6 and NAT traversal/relay are abstracted behind the transport interface.

## Unreal Engine 5-style native implementation
Provide an original Unreal Engine 5-oriented C++ implementation layer rather than copying Unreal source. The design mirrors documented UE networking concepts: authoritative server, dedicated/listen/client modes, replicated gameplay state, RPC-style commands, relevance/priority filtering, prediction/reconciliation, replay and network emulation. Epic documents client-server authority and replication as core UE multiplayer concepts.

The native C++ layer includes engine-facing interfaces for:
- GameMode/GameState-like authoritative match state;
- PlayerController/Pawn-like ownership and input routing;
- Actor-like replicated entities;
- Character movement and prediction;
- weapon/projectile simulation;
- objective/round state;
- replication channels and relevancy;
- dedicated-server build target;
- listen-server build target;
- client build target;
- network emulation tests for latency, jitter, packet loss and reordering.

No Unreal Engine source code is vendored unless separately permitted by its license; adapters target the official engine APIs.

## Rendering architecture
A renderer-neutral contract feeds adapters for Unreal Engine C++, Unity C#, native C++ Vulkan/OpenGL/Direct3D, WebGPU/Three.js, Godot, O3DE, Bevy/Rust, Defold/Lua, Swift/Metal, Kotlin/Android and Flutter/Impeller. High-fidelity rendering is owned by appropriate native engines; other languages provide services, mobile clients, servers, AI, tooling, content processing or adapters.

## Original AAA asset pipeline
Create an original asset pipeline for all game families:
- modular competitive FPS maps;
- RTS maps and terrain;
- voxel/sandbox blocks and structures;
- characters, equipment and props;
- vehicles and drones;
- weapons and original attachments;
- foliage, rocks, buildings and interiors;
- UI/HUD/iconography;
- procedural materials and textures;
- skeletal rigs and movement/animation state machines;
- LOD tiers and mobile variants;
- collision/navmesh/proxy meshes;
- map lighting probes and reflection data.

Asset manifests record source, author, license, license URL, acquisition date, SHA-256, modifications, attribution requirements and redistribution restrictions. Original/generated assets are marked as such.

Proprietary Counter-Strike, Roblox and Minecraft assets are not bundled. Roblox documentation makes clear that creators must respect IP rights and its licensed IP catalog is permission-based; Minecraft/third-party proprietary assets likewise require applicable rights. Public-domain/CC0 assets such as Kenney assets may be used where the individual asset license permits the intended redistribution.

## VFX
Shared VFX schema and original content include:
- muzzle flashes, tracers and impacts;
- smoke, fire, sparks and explosions;
- debris and destruction;
- blood-free competitive impact alternatives plus configurable accessibility effects;
- weather, dust, sand, rain and snow;
- volumetric fog and atmospheric effects;
- water/terrain effects;
- decals;
- GPU particles;
- screen-space/post-processing effects;
- lighting/day-night;
- environmental particles;
- LOD and mobile fallback tiers.

## Audio and voice
Audio metadata and original/licensed content cover weapons, impacts, vehicles, explosions, UI, environment, footsteps, ambience, music, radio/comms, commander voices and NPC dialogue. Include spatial/3D audio, occlusion, obstruction, dynamic mixing, distance curves, reverb zones, voice prioritization and mobile compression. Generated voice is used only under applicable terms and is clearly tracked in provenance manifests.

## Movement and animation
Provide a shared movement state contract with:
- idle/walk/run/sprint;
- crouch/prone where enabled;
- jump/fall/land;
- vault/climb;
- aim/fire/reload/switch;
- damage/recovery;
- swim/vehicle movement where applicable;
- animation montage/event markers;
- root-motion policy;
- network prediction state;
- deterministic gameplay movement versus cosmetic animation separation.

## Strategy simulation
Entities: player, commander, squad, unit, building, resource node, production queue, technology, ability, projectile, vehicle, aircraft, ship, territory, objective, faction, diplomacy relation, logistics route, fog-of-war cell.

Requirements: deterministic ticks, deterministic numeric policy, pathfinding, formations, line of sight, cover, economy, production, research, construction, damage/repair, supply/logistics, objectives and replay serialization.

## Sandbox/voxel simulation
Use chunk-based deterministic world storage with block palette IDs, procedural generation seeds, entity components, lighting, fluid simulation, crafting, inventory, automation/circuit components, mobs/NPCs, structures and permission-controlled UGC. Networking uses chunk streaming, interest management, entity replication and server validation.

## FPS/RTS/sandbox bridge
A shared world state can be observed from strategic, tactical, first-person and sandbox views. Commanders issue orders while players can enter soldiers or vehicles; sandbox users can manipulate authorized world objects. The authoritative simulation remains the source of truth.

## RNN/LLM integration
RNN services: player sequence prediction, unit movement prediction, threat forecasting, resource-flow forecasting, tactical formation prediction, anomaly detection and network telemetry prediction. LLM services: commander assistant, mission briefings, strategy explanation, natural-language tactical orders, replay analysis, NPC dialogue, dynamic objective authoring and narrative assistance. AI output is advisory and cannot directly override authoritative simulation.

## Mobile
Use shared contracts with touch controls, virtual joystick/action layouts, adaptive UI, 30/60 FPS profiles, thermal/battery budgets, asset streaming, compressed textures/audio, low-memory scene variants, offline campaign/skirmish where practical, reconnect-aware multiplayer and Android/iOS services. Defold, Unity, Godot, native Kotlin/Swift and Flutter are used according to workload.

## Repository layout
```text
game-store/vanguard/
game-store/sandbox/
competitive-fps/
strategy/
rendering/strategy/
rendering/fps/
rendering/sandbox/
multiplayer/core/
multiplayer/client-server/
multiplayer/peer-to-peer/
multiplayer/hybrid/
multiplayer/transports/
audio/
vfx/
assets/
assets/manifests/
assets/provenance/
movement/
neural/
tools/
tests/
```

Language implementations follow existing C++, Unreal5, Unity3D, desktop, Node.js, Java, Python, JavaScript, TypeScript, Apple/Swift, Kotlin, Flutter, web and related repository trees.

## Testing
Cover deterministic simulation, movement prediction, weapon/combat authority, round transitions, economy, pathfinding, networking, P2P failure modes, reconnect, replay determinism, asset-manifest validation, audio/VFX-manifest validation, renderer smoke tests and mobile budget profiles. Network tests must emulate latency, jitter, loss and reordering.

## Security/IP
Never ship proprietary game assets without rights. Preserve license notices. Treat network clients as untrusted. Keep wallet secrets out of gameplay/network/save data. Keep AI advisory and sandboxed. Validate multiplayer commands server-side. Rate-limit P2P/session negotiation and never trust client-reported damage, position, inventory or match results in competitive modes.

## Acceptance criteria
Both BizX and BizXtreme must contain synchronized contracts/documentation, runnable reference implementations for supported runtimes, competitive tactical FPS and sandbox/voxel reference architecture, multiplayer client/server and P2P protocol definitions, original FPS/strategy/sandbox storyboards, original or legally redistributable assets, VFX/audio/voice schemas, movement contracts, tests and CI validation. Build-success claims require actual verification evidence.
