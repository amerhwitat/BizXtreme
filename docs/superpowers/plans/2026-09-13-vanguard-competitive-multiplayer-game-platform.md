# Vanguard Competitive Multiplayer Game Platform Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the original Vanguard competitive tactical FPS, shared multiplayer stack, sandbox/voxel layer, original AAA asset/VFX/audio pipeline, and renderer/runtime adapters in BizXtreme.

**Architecture:** Establish one deterministic simulation and transport-independent protocol contract, then implement authoritative client/server, listen-server, LAN and explicitly scoped P2P/hybrid modes behind the same interfaces. Native C++/Unreal-style code owns high-fidelity gameplay/rendering adapters; C#, Rust, Java, Python, Node.js/TypeScript, Kotlin, Swift, Dart and web runtimes consume stable contracts rather than pretending to be the same renderer.

**Tech Stack:** C++17/20, Unreal Engine 5 public APIs, CMake, C#, Unity, Rust, Java, Python, Node.js/TypeScript, Kotlin, Swift, Dart/Flutter, WebGPU/WebGL/Three.js, Godot, UDP/QUIC/WebSocket/WebRTC adapters, JSON/MessagePack-style schemas, GitHub Actions.

**Spec:** `docs/superpowers/specs/2026-09-13-vanguard-multigen-game-platform-design.md`

## Global Constraints

- The competitive/ranked path is server-authoritative.
- P2P is an explicit cooperative/private mode and never silently replaces competitive authority.
- Clients are untrusted; never accept client-reported damage, inventory, position, match result or objective completion without server validation.
- Proprietary Counter-Strike, Roblox and Minecraft source code and assets are not bundled.
- Imported external assets require provenance, license, source, acquisition date, SHA-256 and redistribution status.
- Prefer original/generated assets and CC0/public-domain assets whose individual license permits redistribution.
- AI output is advisory and cannot directly override authoritative simulation.
- Build-success claims require actual verification evidence.

---

### Task 1: Repository and Contract Inventory

**Files:**
- Inspect: existing `README.md`, `docs/`, language roots, `.github/workflows/`
- Create: `competitive-fps/README.md`
- Create: `multiplayer/README.md`
- Create: `assets/README.md`

**Interfaces:**
- Consumes: existing BizXtreme game/rendering/network conventions.
- Produces: stable directory ownership and implementation matrix for subsequent tasks.

- [ ] **Step 1: Inventory existing roots and CI workflows**
- [ ] **Step 2: Record the existing language/runtime entry points in the three README files**
- [ ] **Step 3: Define the canonical cross-runtime schema locations**
- [ ] **Step 4: Validate no existing path is silently repurposed**
- [ ] **Step 5: Commit**

---

### Task 2: Deterministic Competitive FPS Core

**Files:**
- Create: `competitive-fps/core/include/vanguard/fps_state.hpp`
- Create: `competitive-fps/core/include/vanguard/round_state.hpp`
- Create: `competitive-fps/core/include/vanguard/movement_state.hpp`
- Create: `competitive-fps/core/include/vanguard/combat_state.hpp`
- Create: `competitive-fps/core/src/fps_state.cpp`
- Create: `competitive-fps/core/src/round_state.cpp`
- Create: `competitive-fps/core/src/movement_state.cpp`
- Create: `competitive-fps/core/src/combat_state.cpp`
- Test: `tests/competitive-fps/core_test.cpp`

**Interfaces:**
- `RoundState transition(RoundState, RoundEvent)`
- `MovementState simulateMovement(MovementInput, MovementState, Tick)`
- `CombatResult resolveShot(const WeaponState&, const ShotInput&, const WorldQuery&)`
- `FpsSnapshot makeSnapshot(const MatchState&)`

- [ ] **Step 1: Write failing tests for round transitions and invalid transitions**
- [ ] **Step 2: Run the tests and verify failure**
- [ ] **Step 3: Implement the minimal deterministic state machines**
- [ ] **Step 4: Add movement and combat deterministic tests**
- [ ] **Step 5: Run the complete core test target**
- [ ] **Step 6: Commit**

---

### Task 3: Shared Multiplayer Protocol

**Files:**
- Create: `multiplayer/protocol/schema/session.json`
- Create: `multiplayer/protocol/schema/input.json`
- Create: `multiplayer/protocol/schema/snapshot.json`
- Create: `multiplayer/protocol/schema/rpc.json`
- Create: `multiplayer/protocol/schema/replay.json`
- Create: `multiplayer/protocol/include/vanguard/net_protocol.hpp`
- Create: `multiplayer/protocol/src/net_protocol.cpp`
- Test: `tests/multiplayer/protocol_test.cpp`

**Interfaces:**
- `encodePacket(Packet) -> ByteBuffer`
- `decodePacket(ByteView) -> Packet`
- `validateClientCommand(ClientCommand) -> ValidationResult`
- `applySnapshot(ClientWorld&, Snapshot) -> void`

- [ ] **Step 1: Write failing encode/decode and schema-validation tests**
- [ ] **Step 2: Run tests and verify failure**
- [ ] **Step 3: Implement versioned packet headers, sequence numbers, channels and capability negotiation**
- [ ] **Step 4: Implement snapshot/delta and RPC command envelopes**
- [ ] **Step 5: Verify malformed, oversized and stale packets are rejected**
- [ ] **Step 6: Commit**

---

### Task 4: Client/Server, Dedicated, Listen and LAN Modes

**Files:**
- Create: `multiplayer/client-server/server/authoritative_server.cpp`
- Create: `multiplayer/client-server/server/authoritative_server.hpp`
- Create: `multiplayer/client-server/client/client_session.cpp`
- Create: `multiplayer/client-server/client/client_session.hpp`
- Create: `multiplayer/client-server/host/listen_server.cpp`
- Create: `multiplayer/client-server/lan/lan_discovery.cpp`
- Test: `tests/multiplayer/client_server_test.cpp`

**Interfaces:**
- `ServerSession::acceptCommand(ClientCommand)`
- `ServerSession::tick(Tick)`
- `ClientSession::submitInput(InputFrame)`
- `ClientSession::applySnapshot(Snapshot)`
- `LanDiscovery::advertise()` / `LanDiscovery::discover()`

- [ ] **Step 1: Write failing authoritative-state and LAN-discovery tests**
- [ ] **Step 2: Run tests and verify failure**
- [ ] **Step 3: Implement server-owned match state and client command validation**
- [ ] **Step 4: Add listen-server and dedicated-server targets**
- [ ] **Step 5: Add LAN discovery without making discovery authoritative**
- [ ] **Step 6: Test reconnect and duplicate command handling**
- [ ] **Step 7: Commit**

---

### Task 5: P2P and Hybrid/Relay Modes

**Files:**
- Create: `multiplayer/peer-to-peer/peer_session.hpp`
- Create: `multiplayer/peer-to-peer/peer_session.cpp`
- Create: `multiplayer/hybrid/relay_session.hpp`
- Create: `multiplayer/hybrid/relay_session.cpp`
- Create: `multiplayer/transports/udp_transport.*`
- Create: `multiplayer/transports/quic_transport.*`
- Create: `multiplayer/transports/webrtc_transport.*`
- Test: `tests/multiplayer/p2p_hybrid_test.cpp`

**Interfaces:**
- `PeerSession::connect(PeerDescriptor)`
- `PeerSession::send(PeerPacket)`
- `RelaySession::connect(AuthorityDescriptor)`
- `Transport::send(ByteView)` / `Transport::receive()`

- [ ] **Step 1: Write failing tests for peer discovery, disconnect and host trust boundaries**
- [ ] **Step 2: Run tests and verify failure**
- [ ] **Step 3: Implement transport-independent P2P session state**
- [ ] **Step 4: Implement relay/hybrid authority selection**
- [ ] **Step 5: Add transport adapters incrementally, starting with UDP**
- [ ] **Step 6: Add QUIC/WebRTC adapters as optional builds when dependencies are available**
- [ ] **Step 7: Verify ranked mode rejects P2P authority**
- [ ] **Step 8: Commit**

---

### Task 6: Prediction, Replication, Replay and Network Emulation

**Files:**
- Create: `multiplayer/replication/replication_graph.hpp`
- Create: `multiplayer/replication/replication_graph.cpp`
- Create: `multiplayer/prediction/client_prediction.hpp`
- Create: `multiplayer/prediction/client_prediction.cpp`
- Create: `multiplayer/replay/replay_writer.*`
- Create: `multiplayer/replay/replay_reader.*`
- Create: `tools/network-emulator/*`
- Test: `tests/multiplayer/replication_prediction_test.cpp`

**Interfaces:**
- `ReplicationGraph::selectRelevantActors(ConnectionId, WorldState)`
- `ClientPrediction::predict(InputFrame)`
- `ClientPrediction::reconcile(AuthoritativeState)`
- `ReplayWriter::append(Event)`
- `ReplayReader::seek(Tick)`

- [ ] **Step 1: Write failing prediction/reconciliation tests**
- [ ] **Step 2: Run tests and verify failure**
- [ ] **Step 3: Implement input buffering and server reconciliation**
- [ ] **Step 4: Implement relevancy/priority/dormancy-style filtering**
- [ ] **Step 5: Implement deterministic replay serialization**
- [ ] **Step 6: Add latency, jitter, loss and reordering emulation**
- [ ] **Step 7: Verify replay determinism under emulated network faults**
- [ ] **Step 8: Commit**

---

### Task 7: Unreal Engine 5-Oriented Native C++ Adapter

**Files:**
- Create: `rendering/fps/unreal5/Source/VanguardFPS/VanguardGameMode.h/.cpp`
- Create: `rendering/fps/unreal5/Source/VanguardFPS/VanguardGameState.h/.cpp`
- Create: `rendering/fps/unreal5/Source/VanguardFPS/VanguardPlayerController.h/.cpp`
- Create: `rendering/fps/unreal5/Source/VanguardFPS/VanguardCharacter.h/.cpp`
- Create: `rendering/fps/unreal5/Source/VanguardFPS/VanguardWeapon.h/.cpp`
- Create: `rendering/fps/unreal5/README.md`

**Interfaces:**
- Engine classes map to the shared simulation/protocol types; engine replication remains an adapter boundary.

- [ ] **Step 1: Write compile-oriented adapter tests/mocks**
- [ ] **Step 2: Verify tests fail before adapter types exist**
- [ ] **Step 3: Implement GameMode/GameState/Controller/Character/Weapon adapters using official public UE APIs**
- [ ] **Step 4: Add replicated properties/RPC boundaries and dedicated/listen/client target configuration**
- [ ] **Step 5: Add network emulation configuration**
- [ ] **Step 6: Build when a compatible Unreal installation is available; otherwise run interface/mocking tests and record the limitation**
- [ ] **Step 7: Commit**

---

### Task 8: Original Maps, Movement, VFX, Audio and Texture Asset Pipeline

**Files:**
- Create: `assets/manifests/vanguard-fps.json`
- Create: `assets/provenance/README.md`
- Create: `assets/procedural/materials/*`
- Create: `assets/procedural/maps/*`
- Create: `vfx/fps/*`
- Create: `audio/fps/*`
- Create: `movement/fps/*`
- Create: `tools/assets/validate_manifest.py`
- Test: `tests/assets/manifest_validator_test.py`

**Interfaces:**
- `validate_manifest(path) -> ValidationReport`
- `MovementProfile.load(profile)`
- `VfxDefinition.load(id)`
- `AudioCue.load(id)`

- [ ] **Step 1: Write failing provenance and schema-validation tests**
- [ ] **Step 2: Run tests and verify failure**
- [ ] **Step 3: Implement manifest validation and SHA-256 checks**
- [ ] **Step 4: Add original/procedural map descriptors and material/texture metadata**
- [ ] **Step 5: Add VFX definitions for muzzle flash, tracer, impact, smoke, fire, dust, weather and destruction**
- [ ] **Step 6: Add original audio/voice cue manifests with spatial/occlusion metadata**
- [ ] **Step 7: Add movement profiles and animation event contracts**
- [ ] **Step 8: Validate all manifests and commit**

---

### Task 9: Sandbox/Voxel Runtime

**Files:**
- Create: `game-store/sandbox/voxel/chunk.hpp/.cpp`
- Create: `game-store/sandbox/voxel/block_registry.hpp/.cpp`
- Create: `game-store/sandbox/voxel/procedural_world.hpp/.cpp`
- Create: `game-store/sandbox/voxel/crafting.hpp/.cpp`
- Test: `tests/sandbox/voxel_test.cpp`

**Interfaces:**
- `Chunk generateChunk(Seed, ChunkCoord)`
- `BlockId BlockRegistry::resolve(Name)`
- `CraftResult craft(RecipeId, Inventory)`

- [ ] **Step 1: Write failing chunk-generation and serialization tests**
- [ ] **Step 2: Run tests and verify failure**
- [ ] **Step 3: Implement deterministic chunk generation and block palette storage**
- [ ] **Step 4: Implement inventory/crafting and entity persistence**
- [ ] **Step 5: Add chunk streaming/interest-management hooks**
- [ ] **Step 6: Commit**

---

### Task 10: Runtime Language Adapters

**Files:**
- Create/modify language-specific adapters under `cpp/`, `csharp/`, `rust/`, `java/`, `python/`, `node/`, `typescript/`, `kotlin/`, `swift/`, `flutter/`, `web/` according to the existing BizXtreme structure.
- Test: one contract test suite per runtime where that runtime already has CI/toolchain support.

**Interfaces:**
- Every adapter exposes the same session/match/asset/VFX/audio contract names through native idioms and delegates authoritative logic to the shared protocol/core.

- [ ] **Step 1: Write contract-conformance tests for each supported runtime**
- [ ] **Step 2: Run each test and record missing toolchains explicitly**
- [ ] **Step 3: Implement the minimal adapter for each available toolchain**
- [ ] **Step 4: Add mobile touch/controller adapters for Kotlin, Swift and Flutter**
- [ ] **Step 5: Add WebRTC/WebSocket browser adapter where supported**
- [ ] **Step 6: Commit**

---

### Task 11: CI, Documentation and Security Validation

**Files:**
- Modify: `.github/workflows/*`
- Modify: `README.md`
- Modify: `docs/*`
- Create: `docs/networking/competitive-multiplayer.md`
- Create: `docs/assets/provenance-policy.md`
- Create: `docs/security/multiplayer-threat-model.md`

- [ ] **Step 1: Add CI jobs for core, protocol, asset manifests and available adapters**
- [ ] **Step 2: Add a network fault-injection test job**
- [ ] **Step 3: Document dedicated, listen, LAN, P2P and hybrid launch flows**
- [ ] **Step 4: Document the proprietary-IP exclusion policy**
- [ ] **Step 5: Run all CI-equivalent local checks**
- [ ] **Step 6: Commit**

---

### Task 12: Final Verification and Review

**Files:**
- Test: all project test targets and CI workflows.
- Review: all changed paths against the design specification.

- [ ] **Step 1: Run every available test/build target**
- [ ] **Step 2: Verify P2P, dedicated, listen and LAN modes separately**
- [ ] **Step 3: Verify packet-loss/jitter/reordering tests**
- [ ] **Step 4: Verify asset provenance manifests**
- [ ] **Step 5: Verify no proprietary Counter-Strike/Roblox/Minecraft assets or source were introduced**
- [ ] **Step 6: Inspect CI results and document any unavailable toolchain builds**
- [ ] **Step 7: Perform code review against the spec**
- [ ] **Step 8: Commit final verified changes**
