# CoffeeMaker
A digital coffee machine coded in Python

copy & paste to run in your IDE or Repl.it

-OR-

To build program:

-use pyinstaller to build an executable
REFERENCE: https://www.pyinstaller.org/
execute with admin rights from the folder containing the 'main.py' file:
Recommended command line argument: 
'pyinstaller --onefile main.py'

-open 'dist' folder
-run main.exe

COMMAND LIST:

Drink Orders:

    espresso: brew an espresso drink
    latte: brew a latte drink
    cappuccino: brew a cappuccino drink

Service commands:

    clear: clear the screen
    off: exit the program (shut the coffee maker off)
    report: display current machine resources
    restock: restocks all resources (water, milk, coffee)
    restock -water: restocks the water
    restock -milk: restocks the milk
    restock -coffee: restocks the coffee
