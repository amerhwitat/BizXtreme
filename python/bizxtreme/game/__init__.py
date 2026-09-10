class GameService:
    def __init__(self):
        self._saves = {}

    def save(self, slot, state):
        self._saves[slot] = state

    def load(self, slot):
        return self._saves.get(slot)
