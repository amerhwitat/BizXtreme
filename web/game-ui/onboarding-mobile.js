export const onboarding = {
  rules(game){ return {screen:'rules',game,requiredBeforeStart:true}; },
  training(game){ return {screen:'training',game,skippable:true}; },
  start(game,profile){ return {screen:'game',game,profile,startedAt:new Date().toISOString()}; }
};
export function mobileControls({onMove=()=>{},onAction=()=>{},onPause=()=>{}}={}) {
  return {safeArea:true,minTouchTarget:44,movement:{side:'left',onInput:onMove},actions:{side:'right',onInput:onAction},pause:{onInput:onPause}};
}
