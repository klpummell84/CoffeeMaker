import machine

maker = machine.CoffeeMachine(machine.MENU, {"water": 300, "milk": 200, "coffee": 100, "money": 0}, True)
while maker.is_on:
    action = input("  What would you like? (espresso/latte/cappuccino) ").lower()
    maker.choose_action(action)
