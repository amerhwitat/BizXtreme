"""Optional RNN/LLM adapter for emulator chat assistance.
PyTorch is optional; this module fails closed when it is unavailable.
"""
class RNNChatAdapter:
    def __init__(self, model=None):
        self.model = model

    def reply(self, text):
        if self.model is None:
            return "[RNN/LLM unavailable] " + text
        return self.model(text)
