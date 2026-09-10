class WalletProvider:
    def __init__(self, provider):
        self.provider = provider

    def request(self, method, params=None):
        if not callable(self.provider):
            raise TypeError("provider must be callable")
        return self.provider({"method": method, "params": [] if params is None else list(params)})
