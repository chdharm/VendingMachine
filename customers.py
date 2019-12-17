class Customer:
   def __init__(self, name):
       self.name = name #Todo: Considering that name is unique , In real time I will use ID from some RDS
       self.total_value = 0
       self.coins = {}
       self.purchased_items = []