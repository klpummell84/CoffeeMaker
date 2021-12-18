import machine
# create coffee machine object and turn it on:
maker = machine.CoffeeMachine(True)
# Code to run while on:
while maker.is_on:
    action = input("  What would you like? (espresso/latte/cappuccino) ").lower()
    maker.choose_action(action)
