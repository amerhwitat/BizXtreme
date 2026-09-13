export class ProgressionProfile {
  constructor(name = 'Player', state = {}) { this.name=String(name||'Player').slice(0,40); this.level=Number.isInteger(state.level)?Math.max(0,state.level):0; this.status=state.status??'new'; this.score=Number.isFinite(state.score)?Math.max(0,state.score):0; this.updatedAt=state.updatedAt??null; }
  update({level=this.level,status=this.status,score=this.score}={}) { this.level=Math.max(this.level,Number.isInteger(level)?level:this.level); this.status=String(status||this.status); this.score=Math.max(this.score,Number.isFinite(score)?score:this.score); this.updatedAt=new Date().toISOString(); return this.save(); }
  save() { return {name:this.name,level:this.level,status:this.status,score:this.score,updatedAt:this.updatedAt,schema:1}; }
  resume(snapshot) { Object.assign(this,new ProgressionProfile(this.name,snapshot)); return this.save(); }
}
export class HallOfFame {
  constructor({threshold=1000,limit=100,entries=[]}={}) { this.threshold=threshold; this.limit=limit; this.entries=[...entries]; }
  submit({name,score,game='default',level=0}={}) { const numericScore=Number(score)||0; if(numericScore<this.threshold)return {eligible:false,threshold:this.threshold,entry:null}; const entry={name:String(name||'Player').slice(0,40),score:numericScore,game,level,recordedAt:new Date().toISOString()}; this.entries.push(entry); this.entries.sort((a,b)=>b.score-a.score); this.entries=this.entries.slice(0,this.limit); return {eligible:true,threshold:this.threshold,entry,rank:this.entries.indexOf(entry)+1}; }
  list(game) { return (game?this.entries.filter(e=>e.game===game):[...this.entries]).sort((a,b)=>b.score-a.score); }
}
