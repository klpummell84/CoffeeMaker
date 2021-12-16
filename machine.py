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
  "money": 0,
}
COINS = {
  "quarters": 0.25,
  "dimes": 0.10,
  "nickels": 0.05,
  "pennies": 0.01,
}
# GLOBAL machine methods:
def clear_screen():
    if name.lower() == 'nt':
        system('cls')
    else:
        system('clear')

# CoffeeMachine class:
class CoffeeMachine:
    """The coffee machine class"""
    def __init__(self, menu, resources, is_on, has_payment=False):
        self.menu = menu
        self.resources = resources
        self.is_on = is_on
        self.has_payment = has_payment

    def get_money(self):
        print("Please insert coins.")
        q = input("how many quarters?: ")
        if q.isdigit():
            q = int(q)
        else:
            print("Invalid entry, returning coins and resetting...")
            return
        d = input("how many dimes?: ")
        if d.isdigit():
            d = int(d)
        else:
            print("Invalid entry, returning coins and resetting...")
            return
        n = input("how many nickels?: ")
        if n.isdigit():
            n = int(n)
        else:
            print("Invalid entry, returning coins and resetting...")
            return
        p = input("how many pennies?: ")
        if p.isdigit():
            p = int(p)
        else:
            print("Invalid entry, returning coins and resetting...")
            return

        self.has_payment = True
        total = COINS["quarters"] * q + COINS["dimes"] * d + COINS["nickels"] * n + COINS["pennies"] * p
        return total

    def report(self):
        water = self.resources["water"]
        milk = self.resources["milk"]
        coffee = self.resources["coffee"]
        till = self.resources["money"]
        return "Water: {} ml\nMilk: {} ml\nCoffee: {} g\nMoney: ${}".format(water, milk, coffee, round(till, 2))

    def restock(self, item=""):
        if item != "":
            self.resources[item] = RESOURCES[item]
            return
        for i in self.resources:
            if i == 'money':
                continue
            self.resources[i] = RESOURCES[i]

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
            self.check_supply(action)
        else:
            print("Invalid entry, try again...")

    def check_supply(self, drink):
        self.has_payment = False
        for i in self.menu[drink]["ingredients"]:
            if not self.resources[i] >= self.menu[drink]["ingredients"][i]:
                print("There is not enough {}.".format(i))
                return
            else:
                continue
        paid = 0
        while not self.has_payment:
            paid = self.get_money()
        if paid >= self.menu[drink]["cost"]:
            ingredients = self.menu[drink]["ingredients"]
            for i in ingredients:
                self.resources[i] -= self.menu[drink]["ingredients"][i]
            self.brew_coffee(drink=drink, payment=paid)
            return
        else:
            print("Insufficient funds, refund given.")
            return

    def brew_coffee(self, drink, payment):
        print("brewing...")
        change = payment - self.menu[drink]["cost"]
        change = round(change, 2)
        # print(self.report())
        if change > float(0):
            payment -= change
            print("Here is ${} in change.".format(change))
        self.resources["money"] += payment
        print("Here is your {}. Enjoy!".format(drink))  # ☕
