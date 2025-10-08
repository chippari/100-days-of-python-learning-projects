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
# >> 2.1. User Can Pay Function ----------------------------------------------------------------------------------------
def user_can_pay(item_cost):
    print(f"Price: ${item_cost}, please insert coins!")
    user_quarters = int(input("> How many quarters?: "))
    user_dimes = int(input("> How many dimes?: "))
    user_nickles = int(input("> How many nickles?: "))
    user_pennies = int(input("> How many pennies?: "))

    user_total = (user_quarters * 0.25) + (user_dimes * 0.10) + (user_nickles * 0.05) + (user_pennies * 0.01)

    if user_total > item_cost:
        change_money = round(user_total - item_cost, 2)
        return True, f"Here is ${change_money} in change."
    else:
        missing_money = round(item_cost - user_total, 2)
        return False, f"Sorry, you don't have enough money. It's missing ${missing_money}"

# >> 2.2. Machine Can Make Function ------------------------------------------------------------------------------------
def machine_can_make(item):
    can_make = False
    item_out_of_stock = ""

    for resource_key in resources:
        if resource_key in MENU[item]["ingredients"]:
            if resources[resource_key] < MENU[item]["ingredients"][resource_key]:
                item_out_of_stock = resource_key
                break
            else:
                resources[resource_key] -= MENU[item]["ingredients"][resource_key]
                can_make = True

    if can_make:
        return True, f"\nItem Chosen: {item}"
    else:
        return False, f"\nSorry, there is not enough {item_out_of_stock}!"

# >> 2.3. Another Item Function ----------------------------------------------------------------------------------------
def another_item():
    another_choice = input("Would you like to purchase another item? (Y/N): ").upper()

    if another_choice == "Y":
        return True
    else:
        return False

# > 3. Main Code -------------------------------------------------------------------------------------------------------

print("Welcome to our Coffee Machine!")

machine_loop = True
while machine_loop:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")

    for key in MENU.keys():
        if user_choice == key:
            can_make_result = machine_can_make(user_choice)
            can_pay_result = user_can_pay(MENU[user_choice]["cost"])

            if can_make_result[0]:
                print(f"{can_make_result[1]}")
                if can_pay_result[0]:
                    print(can_pay_result[1])
                    print(f"Here is your {user_choice}. Enjoy!")
                    machine_money_earned = MENU[user_choice]["cost"]
                else:
                    print(can_pay_result[1])
            else:
                print(can_make_result[1])

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
