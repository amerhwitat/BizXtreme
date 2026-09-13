from dataclasses import dataclass
from datetime import datetime, timezone

@dataclass
class ProgressionProfile:
    name: str = "Player"
    level: int = 0
    status: str = "new"
    score: int = 0
    updated_at: str | None = None
    def update(self, level=None, status=None, score=None):
        if isinstance(level,int): self.level=max(self.level,level)
        if status: self.status=str(status)
        if isinstance(score,(int,float)): self.score=max(self.score,int(score))
        self.updated_at=datetime.now(timezone.utc).isoformat(); return self.save()
    def save(self): return {"schema":1,"name":self.name[:40],"level":self.level,"status":self.status,"score":self.score,"updatedAt":self.updated_at}

class HallOfFame:
    def __init__(self, threshold=1000, limit=100, entries=None): self.threshold=threshold; self.limit=limit; self.entries=list(entries or [])
    def submit(self,name="Player",score=0,game="default",level=0):
        score=int(score)
        if score<self.threshold:return {"eligible":False,"threshold":self.threshold,"entry":None}
        entry={"name":str(name)[:40],"score":score,"game":game,"level":level,"recordedAt":datetime.now(timezone.utc).isoformat()}; self.entries.append(entry); self.entries.sort(key=lambda e:e["score"],reverse=True); self.entries=self.entries[:self.limit]; return {"eligible":True,"threshold":self.threshold,"entry":entry,"rank":self.entries.index(entry)+1}
    def list(self,game=None): return sorted([e for e in self.entries if game is None or e.get("game")==game],key=lambda e:e["score"],reverse=True)
