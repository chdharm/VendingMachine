class Coins:
    def __init__(self):
        self.VALID_COINS = [10, 50, 100, 500]

    def is_valid_coin(self,coin):
        if coin in self.VALID_COINS:
            return True
        return False

    def can_coin_be_used(self, coin, all_coins_in_vending_machine):
        if self.is_valid_coin(coin) is False:
            return False
        if all_coins_in_vending_machine["10"] ==0:
            if coin > 10:
                return False
        elif all_coins_in_vending_machine["100"] ==0:
            if coin > 100:
                return False
        return True

    @staticmethod
    def is_change_possible(amount, all_coins_in_vending_machine):
        if all_coins_in_vending_machine["10"] < 9:
            return False
        if all_coins_in_vending_machine["100"] < 4:
            return False
        if amount%10 != 0:
            return False
        return True