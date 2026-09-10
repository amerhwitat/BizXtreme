from bizxtreme.core import BizXtremeCore

class BizXtremeApi:
    def __init__(self, core=None):
        self.core = core or BizXtremeCore()

    def health(self):
        return self.core.health()
