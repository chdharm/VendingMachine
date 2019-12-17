from .items import Items
class VendingMachine:

    def __init__(self, ):
        self.total_value = 0
        self.coins = {}
        self.provisional_coin_storage = {}

    def admin_update_quantity(self):
        pass

    def admin_add_stock(self, data):
        name = data.get("name")
        _req_data = {
            "name": name,
            "price": data.get("price"),
            "quantity":data.get("quantity")
        }
        if name not in Items.ITEM_LIST.keys():
           Items.ITEM_LIST.update(_req_data)

    def admin_add_vm_coins(self):
        pass

    def add_coin(self,coin):
        if coin is not in VendingMachine.VALID_COINS:
            print("Coin addition is failed !")
            return False
        self.total_value += coin
        if self.coins.get(coin):
            self.coins[coin] +=1
        else:
            self.coins[coin] = 1
        print("Coin added successfully !")
        return True
