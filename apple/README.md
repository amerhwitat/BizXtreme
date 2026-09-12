# Apple application

BizXtreme Apple source uses native SwiftUI/Xcode with shared domain/state boundaries. iOS/iPadOS targets use `iosArm64` and `iosSimulatorArm64`; macOS uses native Xcode targets. Existing game/WebGL/crypto/network modules remain intact and are integrated through explicit interfaces.

IPA generation requires macOS + Xcode. Camera/microphone are explicit, permission-gated capabilities; authenticated P2P remains the communications boundary.
