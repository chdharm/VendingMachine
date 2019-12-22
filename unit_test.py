import unittest
from coins import Coins
from items import Items
from customers import Customer
from vendingmachine import VendingMachine


class VendingMachineUnitTesting(unittest.TestCase):

    def test_is_valid_coin_10(self):
        coin_obj = Coins()
        coin = 10
        # Passing 10 which is valid coin
        self.assertEqual(True, coin_obj.is_valid_coin(coin))

    def test_is_valid_coin_30(self):
        coin_obj = Coins()
        coin = 10
        # Passing 30 which is invalid coin
        coin = 30
        self.assertEqual(False, coin_obj.is_valid_coin(coin))


if __name__ == '__main__':
    unittest.main()