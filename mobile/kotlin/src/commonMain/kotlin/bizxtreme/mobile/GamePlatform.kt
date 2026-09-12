package bizxtreme.mobile

data class GameEntry(val id:String,val title:String,val dimensions:String,val assetPack:String,val modes:List<String>)
data class SaveSnapshot(val slot:String,val gameId:String,val score:Long,val payloadHash:String,val createdEpochMs:Long)
data class WalletProfile(val providerId:String,val addressLabels:List<String>,val backupVersion:Int=1)
class GamePlatform{
 private val catalog=listOf(
  GameEntry("poker-holdem","Texas Hold’em Poker","2D","card-deck-premium",listOf("single-player","online-multiplayer")),
  GameEntry("blackjack","Blackjack","2D","card-deck-premium",listOf("single-player","online-multiplayer")),
  GameEntry("classic-cards","Classic Card Suite","2D","card-deck-premium",listOf("single-player","local-multiplayer","online-multiplayer")),
  GameEntry("trex-runner","T-Rex Runner","2D","trex-original",listOf("single-player","hall-of-fame")),
  GameEntry("story-2d","2D Storyboard Adventure","2D","open-assets-2d",listOf("single-player")),
  GameEntry("world-3d","3D World Builder","3D","open-assets-3d",listOf("single-player")),
  GameEntry("time-4d","4D Timeline Quest","4D","open-assets-4d",listOf("single-player"))
 )
 fun games():List<GameEntry> = catalog
 fun walletSetup(providerId:String,labels:List<String>)=WalletProfile(providerId,labels)
 fun snapshot(slot:String,gameId:String,score:Long,hash:String,now:Long)=SaveSnapshot(slot,gameId,score,hash,now)
}
