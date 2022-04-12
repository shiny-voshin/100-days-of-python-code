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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
profit = 0

# TODO: 1. Prompt user by asking "What would you like? (espresso/latte/cappuccino): "
# a.check the user's input to decide what to do next.
# b. The prompt should show every time action has completed, e.g. once the drink is dispensed.
# The prompt should show again to serve the next customer.


def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}. Contact an Admin.")
            return False
    return True


def process_coins():
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    print(total)
    return total


def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is your {change}")
        global profit
        profit += drink_cost
        return True
    else:
        print(f"Sorry that's not enough money. Money refunded")
        return False


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}")


machine_on = True

while machine_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice.lower() == "espresso":
        print(f"You Selected {choice}.")
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
        print(drink)
    elif choice.lower() == "latte":
        print(f"You Selected {choice}.")
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
        print(drink)
    elif choice.lower() == "cappuccino":
        print(f"You Selected {choice}.")
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
        print(drink)
    elif choice.lower() == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}ml")
        print(f"money : {profit}")
    elif choice.lower() == "off":
        print("Powering Off...")
        machine_on = False
    else:
        print(f"You did not select from the listed items.")
