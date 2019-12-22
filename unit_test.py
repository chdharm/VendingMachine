import unittest
from coins import Coins
from items import Items
from customers import Customer
from vendingmachine import VendingMachine


class VendingMachineUnitTesting(unittest.TestCase):

    # -------- Coin Section ------------ #
    def test_is_valid_coin_10(self):
        coin_obj = Coins()
        coin = 10
        self.assertEqual(True, coin_obj.is_valid_coin(coin))

    def test_is_valid_coin_30(self):
        coin_obj = Coins()
        coin = 30
        self.assertEqual(False, coin_obj.is_valid_coin(coin))

    def test_is_change_possible_with_correct_data(self):
        all_available_coins = {"10": 10, "50": 10, "100": 20, "500": 30}
        self.assertEqual(True, Coins.is_change_possible(10, all_available_coins))

    def test_is_change_possible_with_incorrect_data(self):
        all_available_coins = {"10": 1, "50": 10, "100": 20, "500": 30}
        self.assertEqual(False, Coins.is_change_possible(10, all_available_coins))

    def test_can_coin_be_used_correct_data(self):
        coin_obj = Coins()
        all_available_coins = {"10": 1, "50": 10, "100": 20, "500": 30}
        self.assertEqual(True, coin_obj.can_coin_be_used(10, all_available_coins))

    def test_can_coin_be_used_incorrect_data(self):
        coin_obj = Coins()
        all_available_coins = {"10": 0, "50": 10, "100": 20, "500": 30}
        self.assertEqual(False, coin_obj.can_coin_be_used(100, all_available_coins))
    # -------- End of Coin Section ------------ #

    # --------


if __name__ == '__main__':
    unittest.main()