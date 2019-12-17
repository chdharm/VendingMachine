if __name__ == '__main__':
    print("Starting the application !!")
    should_exit = False
    last_action = None
    vm = VendingMachine
    while should_exit is False:
        if last_action is None: #Todo: User is new
            _input = input("Please enter the command!")
            print(_input)
        elif last_action == "ready_to_select_items":
            _input = input("Please enter the command!")
            print(_input)
        elif