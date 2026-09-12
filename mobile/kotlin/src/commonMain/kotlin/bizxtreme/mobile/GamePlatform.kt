package bizxtreme.mobile

data class GameEntry(val id: String, val title: String, val dimensions: String, val assetPack: String)
data class SaveSnapshot(val slot: String, val gameId: String, val score: Long, val payloadHash: String, val createdEpochMs: Long)
data class WalletProfile(val providerId: String, val addressLabels: List<String>, val backupVersion: Int = 1)

class GamePlatform {
    private val catalog = listOf(
        GameEntry("story-2d", "2D Storyboard Adventure", "2D", "open-assets-2d"),
        GameEntry("world-3d", "3D World Builder", "3D", "open-assets-3d"),
        GameEntry("time-4d", "4D Timeline Quest", "4D", "open-assets-4d")
    )
    fun games(): List<GameEntry> = catalog
    fun walletSetup(providerId: String, labels: List<String>) = WalletProfile(providerId, labels)
    fun snapshot(slot: String, gameId: String, score: Long, hash: String, now: Long) = SaveSnapshot(slot, gameId, score, hash, now)
}
