# BizXtreme Mobile Unified Application

Unified mobile architecture for BizXtreme. Android, iOS, Flutter, and React Native adapters share the same gameplay/economy state contract while preserving native platform capabilities.

## Targets

- Android: Kotlin + Jetpack Compose
- iOS: Swift + SwiftUI
- Flutter/Dart
- React Native/TypeScript

## Shared capabilities

- Tycoon/game state and progression
- virtual BIZ economy/ledger
- offline-first session state
- rendering capability selection
- network session boundary
- serialization-ready state model

Real cryptocurrency settlement remains outside the virtual game ledger and must go through explicitly authorized wallet/payment infrastructure.

## Existing projects

The existing `kotlin/mobile`, `apple`, and other mobile-related projects remain intact. `MobileUnified` provides the common contract and adapter layer so they can evolve without duplicating game rules.
