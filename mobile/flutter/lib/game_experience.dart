class TouchLayout { final bool safeArea; final double minTouchTarget; const TouchLayout({this.safeArea=true,this.minTouchTarget=44}); }
class OnboardingState { final bool rulesRequired, trainingAvailable, trainingSkippable; const OnboardingState({this.rulesRequired=true,this.trainingAvailable=true,this.trainingSkippable=true}); }
class PlayerProgress { final String name, gameId, status; final int level, score; const PlayerProgress({this.name='Player',this.gameId='default',this.status='new',this.level=0,this.score=0}); }
class MobileGameExperience { const MobileGameExperience(); TouchLayout controls()=>const TouchLayout(); OnboardingState onboarding()=>const OnboardingState(); PlayerProgress saveProgress(PlayerProgress progress)=>progress; }
