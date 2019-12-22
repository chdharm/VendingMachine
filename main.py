from coins import Coins
from items import Items
from customers import Customer
from vendingmachine import VendingMachine


if __name__ == '__main__':
    print("Starting the application !!")
    should_exit = False
    last_action = None
    vm_machine = VendingMachine()
    selected_item = None
    while should_exit is False:
        if last_action is None:
            _input = input("Please enter the command!\n")
            print(type(_input))
            if _input[:1] == "1":
                _inserted_amt = int(_input.split(" ")[1])
                print("_inserted_amt:", _inserted_amt)
            elif _input[:1] == "2":
                _item_no_request = int(_input.split(" ")[1])
                print("_item_no_request:", _item_no_request)
            elif _input[:1] == "3":
                # Get the item
                pass
            elif _input[:1] == "4":
                # Return Coins
                pass
            elif _input[:1] == "5":
                # Get the returned coin
                pass
        elif last_action == "ready_to_select_items":
            _input = input("Please enter the command!")
            print(_input)
        else:
            pass