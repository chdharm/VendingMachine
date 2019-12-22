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

    # --------- Vending Machine --------- #
    def test_admin_update_quantity_with_correct_data(self):
        vm_m = VendingMachine()
        name = "Banana"
        item_detail = list(filter(lambda x: x["name"] == name, vm_m.ITEM_LIST))
        item_detail = item_detail[0]
        previous_quantity = item_detail.get("quantity")

        vm_m.admin_update_quantity({"name": "Banana", "quantity": 20, "price": 30})
        item_detail = list(filter(lambda x: x["name"] == name, vm_m.ITEM_LIST))
        item_detail = item_detail[0]
        new_quantity = item_detail.get("quantity")
        self.assertEqual(True, previous_quantity < new_quantity)

    def test_admin_update_quantity_with_incorrect_data(self):
        vm_m = VendingMachine()
        name = "Banana"
        item_detail = list(filter(lambda x: x["name"] == name, vm_m.ITEM_LIST))
        item_detail = item_detail[0]
        previous_quantity = item_detail.get("quantity")

        vm_m.admin_update_quantity({"name": "Banana", "quantity": 0, "price": 30})
        item_detail = list(filter(lambda x: x["name"] == name, vm_m.ITEM_LIST))
        item_detail = item_detail[0]
        new_quantity = item_detail.get("quantity")
        self.assertEqual(False, previous_quantity < new_quantity)

    def test_admin_add_stock_with_correct_data(self):
        vm_m = VendingMachine()
        name = "Blueberry"
        vm_m.admin_add_stock({"name": name, "quantity": 0, "price": 30})
        item_detail = list(filter(lambda x: x["name"] == name, vm_m.ITEM_LIST))
        if item_detail and len(item_detail) > 0:
            item_detail = item_detail[0]
            item = item_detail.get("name")
        else:
            item = None
        self.assertEqual(True, item is not None)

    def test_admin_add_stock_with_incorrect_data(self):
        vm_m = VendingMachine()
        name = "Blackberry"
        vm_m.admin_add_stock({"price": 30})
        item_detail = list(filter(lambda x: x["name"] == name, vm_m.ITEM_LIST))
        if item_detail and len(item_detail) > 0:
            item_detail = item_detail[0]
            item = item_detail.get("name")
        else:
            item = None
        self.assertEqual(False, item is not None)

    def test_admin_add_vending_machine_coins_with_correct_data(self):
        vm_m = VendingMachine()
        previous_count_10_coin = vm_m.coins.get("10")
        vm_m.admin_add_vending_machine_coins({"10": 100})
        new_count_10_coin = vm_m.coins.get("10")
        self.assertEqual(True, new_count_10_coin > previous_count_10_coin)

    def test_admin_add_vending_machine_coins_with_incorrect_data(self):
        vm_m = VendingMachine()
        previous_count_10_coin = vm_m.coins.get("10")
        vm_m.admin_add_vending_machine_coins({"10": 0})
        new_count_10_coin = vm_m.coins.get("10")
        self.assertEqual(False, new_count_10_coin > previous_count_10_coin)

    def test_add_coin_with_correct_data(self):
        vm_m = VendingMachine()
        previous_count_10_coin = vm_m.provisional_coin_storage.get("10")
        vm_m.add_coin("10")
        new_count_10_coin = vm_m.provisional_coin_storage.get("10")
        self.assertEqual(True, new_count_10_coin > previous_count_10_coin)

    def test_add_coin_with_incorrect_data(self):
        vm_m = VendingMachine()
        previous_count_10_coin = vm_m.provisional_coin_storage.get("10")
        vm_m.add_coin("1000")
        new_count_10_coin = vm_m.provisional_coin_storage.get("10")
        self.assertEqual(False, new_count_10_coin > previous_count_10_coin)

    # ----------------------------------- #


if __name__ == '__main__':
    unittest.main()