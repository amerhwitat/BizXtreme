class CoinRegistry:
    def __init__(self):
        self._chains = {}

    def register(self, symbol, network):
        self._chains[symbol] = network

    def network(self, symbol):
        return self._chains.get(symbol)
