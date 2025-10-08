# > Coffee Machine Project ---------------------------------------------------------------------------------------------
from platform import machine

# > 1. Dictionaries ----------------------------------------------------------------------------------------------------
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

machine_money_earned = 0

# > 2. Functions -------------------------------------------------------------------------------------------------------
# >> 2.1. User Change Function -----------------------------------------------------------------------------------------
def user_change(item_cost):
    print("Please insert coins!")
    user_quarters = int(input("How many quarters?: "))
    user_dimes = int(input("How many dimes?: "))
    user_nickles = int(input("How many nickles?: "))
    user_pennies = int(input("How many pennies?: "))

    user_total = (user_quarters * 0.25) + (user_dimes * 0.10) + (user_nickles * 0.05) + (user_pennies * 0.01)

    if user_total > item_cost:
        change_money = round(user_total - item_cost, 2)
        return print(f"Here is ${change_money} in change.")
    else:
        return print("Sorry, you don't have enough money.")

# >> 2.2. Can Make Item Function ---------------------------------------------------------------------------------------
def can_make_item(item):
    for resource_key in resources:
        for item_key in item["ingredients"]:
            if item_key == resource_key:
                if resources[resource_key] < item["ingredients"][resource_key]:
                    print(f"Sorry, there is not enough {resources[resource_key]}!")
                else:
                    resources[resource_key] -= item["ingredients"][resource_key]

# > 3. Main Code -------------------------------------------------------------------------------------------------------

print("Welcome to our Coffee Machine!")

machine_loop = True
while machine_loop:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")

    for key in MENU.keys():
        if user_choice == key:
            can_make_item(MENU[user_choice])
            user_change(MENU[user_choice]["cost"])
            print(f"Here is your {user_choice}. Enjoy!")

            machine_money_earned = MENU[user_choice]["cost"]

    if user_choice == "report":
        print(">> Coffee Machine Report")
        for key, value in resources.items():
            if key == "water" or key == "milk":
                print(f"{key.capitalize()}: {value}ml")
            elif key == "coffee":
                print(f"{key.capitalize()}: {value}g")

        print(f"Money: ${machine_money_earned}")
    elif user_choice == "off":
        print(">> The Coffee Machine is now off for maintainers!")
        machine_loop = False

# ----------------------------------------------------------------------------------------------------------------------
