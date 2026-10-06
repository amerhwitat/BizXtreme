"""RNN/LLM adapter shared with Aurora.
The adapter accepts an injected model callable and keeps guest/emulator state isolated.
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Callable, Optional

@dataclass
class ModelResult:
    text: str
    provider: str
    confidence: float = 0.0

class RNNChatAdapter:
    def __init__(self, model: Optional[Callable[[str], str]] = None):
        self.model = model
        self.events = []

    def learn_event(self, event: dict) -> None:
        self.events.append({k: event[k] for k in ("page","element","action","timestamp") if k in event})
        self.events = self.events[-2000:]

    def reply(self, text: str) -> ModelResult:
        if self.model is None:
            return ModelResult("[RNN/LLM backend not loaded] " + text, "unavailable", 0.0)
        value = self.model(text)
        return ModelResult(str(value), "injected-model", 1.0)
