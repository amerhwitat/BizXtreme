package bizxtreme.mobile

data class TouchLayout(val safeArea:Boolean=true,val minTouchTargetDp:Int=44,val movementSide:String="left",val actionSide:String="right",val pauseVisible:Boolean=true)
data class OnboardingState(val rulesRequired:Boolean=true,val trainingAvailable:Boolean=true,val trainingSkippable:Boolean=true)
data class PlayerProgress(val name:String="Player",val gameId:String="default",val level:Int=0,val status:String="new",val score:Long=0)
class MobileGameExperience { fun controls()=TouchLayout(); fun onboarding()=OnboardingState(); fun saveProgress(progress:PlayerProgress)=progress }
