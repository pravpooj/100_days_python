from doctest import OutputChecker
from sysconfig import is_python_build
from unicodedata import is_normalized
from coffee_main import  MENU
from coffee_main import resources

def is_resources_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"sorry there is not enough {item}")
            return False
    return True
def process_coins():
    print("Please insert the coins")
    total = int(input("How many quarters?:"))* 0.25
    total += int(input("How many dimes?:"))* 0.1
    total += int(input("How many nickles?:"))* 0.05
    total += int(input("How many pennies?:"))* 0.05
    return total

def is_transaction_succesful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost,2)
        print(f"here is the ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money, please collect the coins")
        return False


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"here is your {drink_name}☕☕☕☕")

profit = 0
is_on = True
while is_on:
    choice = input(f"what would you like to order from below menu: \n Espresso, Latte, Cappuccino ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resources_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_succesful(payment,drink["cost"]):

                make_coffee(choice, drink["ingredients"])


