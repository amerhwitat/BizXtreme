from dataclasses import dataclass, field
from typing import Any

DISCIPLINES = ["ml", "dl", "rl", "symbolic_ai", "computer_vision", "nlp"]

@dataclass
class AIJob:
    discipline: str
    task: str
    data_kind: str
    framework: str | None = None
    parameters: dict[str, Any] = field(default_factory=dict)
    provenance: dict[str, Any] = field(default_factory=dict)

    def validate(self):
        if self.discipline not in DISCIPLINES:
            raise ValueError("unsupported AI discipline")
        if not self.task.strip() or not self.data_kind.strip():
            raise ValueError("task and data_kind are required")
        return self

class AIFabric:
    def job(self, discipline, task, data_kind, **kwargs):
        return AIJob(discipline, task, data_kind, **kwargs).validate()
