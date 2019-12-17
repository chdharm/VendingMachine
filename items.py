from .coins import Coins
class Items:
    def __init__(self):
        self.GLOBAL_ITEM_LIST = [
            {
                "name": "Banana",
                "price": 30,
                "quantity": 2
            },
            {
                "name": "Papaya",
                "price": 20,
                "quantity": 6
            },
            {
                "name": "Guava",
                "price": 50,
                "quantity": 2
            },
            {
                "name": "Oil",
                "price": 60,
                "quantity": 9
            },
            {
                "name": "Pepsi",
                "price": 90,
                "quantity": 3
            },
            {
                "name": "Coke",
                "price": 100,
                "quantity": 20
            },
            {
                "name": "Pen",
                "price": 120,
                "quantity": 200
            },
            {
                "name": "Notebook",
                "price": 150,
                "quantity": 5
            },
            {
                "name": "Pen-drive",
                "price": 170,
                "quantity": 2
            },
            {
                "name": "File",
                "price": 200,
                "quantity": 2
            },
            {
                "name": "Wire",
                "price": 300,
                "quantity": 1
            },
            {
                "name": "Medicine",
                "price": 400,
                "quantity": 2
            },
            {
                "name": "Whitener",
                "price": 450,
                "quantity": 2
            },
            {
                "name": "Gun",
                "price": 500,
                "quantity": 2
            },
            {
                "name": "pizza",
                "price": 330,
                "quantity": 20
            },
            {
                "name": "burger",
                "price": 270,
                "quantity": 20
            },
        ]
        self.ITEM_LIST = []

    def is_item_can_be_purchased(self, item, customer_coins_provisional_store):
        item_detail = self.ITEM_LIST.get(item)
        if item_detail.get("quantity") == 0:
            return False
        _item_price = item_detail.get("price")
        _total_amount = 0
        coin_obj = Coins()
        for coin in customer_coins_provisional_store:
            if coin_obj.can_coin_be_used(coin, customer_coins_provisional_store):
                _total_amount += coin
        if _total_amount >= _item_price:
            return True
        return False
