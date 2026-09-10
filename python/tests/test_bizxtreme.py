import unittest
from bizxtreme import BizXtremeCore, WalletProvider, CoinRegistry, GameService

class BizXtremeTests(unittest.TestCase):
    def test_health(self):
        self.assertEqual(BizXtremeCore().health()["runtime"], "python")

    def test_wallet(self):
        wallet = WalletProvider(lambda payload: payload["method"])
        self.assertEqual(wallet.request("eth_chainId"), "eth_chainId")

    def test_coin_registry(self):
        registry = CoinRegistry(); registry.register("BTC", "bitcoin")
        self.assertEqual(registry.network("BTC"), "bitcoin")

    def test_game_save(self):
        game = GameService(); game.save("slot1", {"level": 1})
        self.assertEqual(game.load("slot1")["level"], 1)

if __name__ == "__main__":
    unittest.main()
