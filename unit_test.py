import unittest
from coins import Coins
from items import Items
from customers import Customer
from vendingmachine import VendingMachine


class VendingMachineUnitTesting(unittest.TestCase):

    # -------- Coin Section ------------ #
    def test_is_valid_coin_with_correct_data(self):
        coin_obj = Coins()
        coin = 10
        self.assertEqual(True, coin_obj.is_valid_coin(coin))

    def test_is_valid_coin_with_incorrect_data(self):
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
    # -------------------------------------- #

    # -------- Item Section ---------- #
    def test_is_item_can_be_purchased_with_correct_data(self):
        item_obj = Items()
        _customer_provision = {
            "10": 30,
            "50": 40,
            "100": 2,
            "500": 3
        }
        self.assertEqual(True, item_obj.is_item_can_be_purchased("Banana", _customer_provision))

    def test_is_item_can_be_purchased_with_incorrect_data(self):
        item_obj = Items()
        _customer_provision = {
            "10": 2,
            "50": 0,
            "100": 0,
            "500": 0
        }
        self.assertEqual(False, item_obj.is_item_can_be_purchased("Banana", _customer_provision))
    # -------------------------------- #


if __name__ == '__main__':
    unittest.main()