from os import system, name

# DATA:
MENU = {
  "espresso": {
    "ingredients": {
      "water": 50,
      "coffee": 18,
    },
    "cost": 1.5,
  },
  "latte": {
    "ingredients": {
      "water": 200,
      "milk": 150,
      "coffee": 24,
    },
    "cost": 2.5,
  },
  "cappuccino": {
    "ingredients": {
      "water": 250,
      "milk": 100,
      "coffee": 24,
    },
    "cost": 3.0,
  }
}
RESOURCES = {
  "water": 300,
  "milk": 200,
  "coffee": 100,
}

# GLOBAL machine methods:
def clear_screen():
    if name.lower() == 'nt':
        system('cls')
    else:
        system('clear')

# CoffeeMachine class:
def get_money():

    valid = False

    def invalid():
        print("Invalid entry, returning coins and resetting...")

    while not valid:
        print("Please insert coins.")
        q = input("how many quarters?: ")
        if q.isdigit():
            q = int(q)
        else:
            invalid()
            continue
        d = input("how many dimes?: ")
        if d.isdigit():
            d = int(d)
        else:
            invalid()
            continue
        n = input("how many nickels?: ")
        if n.isdigit():
            n = int(n)
        else:
            invalid()
            continue
        p = input("how many pennies?: ")
        if p.isdigit():
            p = int(p)
        else:
            invalid()
            continue
        valid = True
    total = 0.25 * q + 0.1 * d + 0.05 * n + 0.01 * p
    return total


class CoffeeMachine:
    """The coffee machine class"""
    def __init__(self, menu, resources, is_on, till=0):
        self.menu = menu
        self.resources = resources
        self.is_on = is_on
        self.till = till

    def report(self):
        water = self.resources["water"]
        milk = self.resources["milk"]
        coffee = self.resources["coffee"]
        till = self.till
        return "Water: {} ml\nMilk: {} ml\nCoffee: {} g\nMoney: ${}".format(water, milk, coffee, till)

    def restock(self, item=""):
        if item != "":
            self.resources[item] = RESOURCES[item]
            return
        for i in self.resources:
            self.resources[i] = RESOURCES[i]

    def validate_payment(self, payment, cost):
        if payment >= cost:
            change = round(payment - cost, 2)
            if change > 0:
                print("Here is ${:,.2f} in change.".format(change))
            self.till += cost
            return True
        print("You're short on payment, refund given.")
        return False

    def choose_action(self, action):
        if action == 'off':
            self.is_on = False
        elif action == 'report':
            print(self.report())
        elif action == 'restock':
            self.restock()
            print("All resources were restocked.")
        elif action.split(" -") == ["restock", "water"]:
            self.restock("water")
            print("Water was restocked.")
        elif action.split(" -") == ["restock", "milk"]:
            self.restock("milk")
            print("Milk was restocked.")
        elif action.split(" -") == ["restock", "coffee"]:
            self.restock("coffee")
            print("Coffee was restocked.")
        elif action == 'clear':
            clear_screen()
        elif action in self.menu:
            if self.check_supply(self.menu[action]["ingredients"]):
                drink = self.menu[action]
                payment = get_money()
                if self.validate_payment(payment, drink["cost"]):
                    self.brew_coffee(drink, action)
        else:
            print("Invalid entry, try again...")

    def check_supply(self, ingredients):
        for i in ingredients:
            if ingredients[i] > self.resources[i]:
                print("Sorry, there is not enough {}.".format(i))
                return False
        return True

    def brew_coffee(self, drink, drink_name):
        print("brewing...")
        for i in drink["ingredients"]:
            self.resources[i] -= drink["ingredients"][i]
        print("Here is your {}. Enjoy!".format(drink_name))  # ☕
