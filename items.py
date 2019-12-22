from coins import Coins


class Items:
    GLOBAL_ITEM_LIST = [
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

    def __init__(self, item_list=None):
        self.ITEM_LIST = item_list if item_list is not None else Items.GLOBAL_ITEM_LIST

    def is_item_can_be_purchased(self, item_name, customer_coins_provisional_store):
        item_detail = list(filter(lambda x: x["name"] == item_name, self.ITEM_LIST))
        if item_detail is None or len(item_detail) < 1:
            return False
        item_detail = item_detail[0]
        if item_detail.get("quantity") == 0:
            return False
        _item_price = item_detail.get("price")
        _total_amount = 0
        coin_obj = Coins()
        for coin in customer_coins_provisional_store:
            if coin_obj.can_coin_be_used(int(coin), customer_coins_provisional_store):
                _total_amount += int(coin) * customer_coins_provisional_store[coin]
        print("Items _total_amount==:", _total_amount)
        if _total_amount >= _item_price:
            return True
        return False
