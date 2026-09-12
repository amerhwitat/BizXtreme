import SwiftUI

public struct BizXtremeAppleApp: Sendable {
    public init() {}
    public let schemaVersion = 1
    public let capabilities = ["authenticated-chat", "voice", "camera", "game-state-sync"]
}

@main
struct BizXtremeAppleMain: App {
    var body: some Scene { WindowGroup { Text("BizXtreme Apple") } }
}
