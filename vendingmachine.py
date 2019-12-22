from items import Items
from coins import Coins


class VendingMachine:

    def __init__(self):
        self.ITEM_LIST = Items.GLOBAL_ITEM_LIST
        self.total_value = 0
        self.coins = {
            "10": 0,
            "50": 0,
            "100": 0,
            "500": 0
        }
        self.provisional_coin_storage = {
            "10": 0,
            "50": 0,
            "100": 0,
            "500": 0
        }

    def admin_update_quantity(self, data):
        name = data.get("name")
        _req_data = {
            "name": name,
            "price": data.get("price"),
            "quantity": data.get("quantity")
        }

        item_detail = list(filter(lambda x: x["name"] == name, self.ITEM_LIST))
        if item_detail is None or len(item_detail) < 1:
            return

        self.ITEM_LIST[self.ITEM_LIST.index(item_detail[0])]["quantity"] += _req_data.get("quantity")
        self.ITEM_LIST[self.ITEM_LIST.index(item_detail[0])]["price"] = _req_data.get("price")

    def admin_add_stock(self, data):
        name = data.get("name")
        _req_data = {
            "name": name,
            "price": data.get("price"),
            "quantity": data.get("quantity")
        }
        item_detail = list(filter(lambda x: x["name"] == name, self.ITEM_LIST))
        if item_detail is None or len(item_detail) < 1:
            self.ITEM_LIST.append(_req_data)

    def admin_add_vending_machine_coins(self, data):
        for _data in data:
            coin_obj = Coins()
            if coin_obj.is_valid_coin(int(_data)):
                self.coins[_data] += data[_data]

    def add_coin(self, coin):
        coin_obj = Coins()
        if coin_obj.is_valid_coin(int(coin)):
            self.provisional_coin_storage[coin] += 1

