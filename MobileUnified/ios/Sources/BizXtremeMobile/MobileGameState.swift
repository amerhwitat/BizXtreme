import Foundation

public struct MobileGameState: Codable, Sendable {
    public var mode: String
    public var cash: Int64
    public var level: Int
    public var score: Int64
    public var bizVirtual: Bool
    public var network: String

    public init(mode: String = "default", cash: Int64 = 10_000) {
        self.mode = mode
        self.cash = cash
        self.level = 1
        self.score = 0
        self.bizVirtual = true
        self.network = "offline"
    }
}

public enum MobileGameEngine {
    public static func start(mode: String = "default", cash: Int64 = 10_000) -> MobileGameState {
        MobileGameState(mode: mode, cash: cash)
    }
}
