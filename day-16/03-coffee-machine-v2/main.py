# > Coffee Machine Project v2 ------------------------------------------------------------------------------------------

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

def coffee_machine_v2():
    print("Welcome to our Coffee Machine!")

    order = 0
    machine_loop = True
    while machine_loop:
        if order == 0:
            user_choice = input(f"What would you like? ({menu.get_items()}): ").lower()
        else:
            user_choice = input(f"\nWould you like anything else? Type ({menu.get_items()}) or Type 'no' to "
                                f"finish your order: ").lower()

        if menu.find_drink(user_choice):
            item = menu.find_drink(user_choice)

            if coffee_maker.is_resource_sufficient(item):
                if money_machine.make_payment(item.cost):
                    coffee_maker.make_coffee(item)

        if user_choice == "report":
            coffee_maker.report()
            money_machine.report()

        if user_choice == "no":
            print("Thank you for choosing our Coffee Machine!")
            machine_loop = False

        order += 1

coffee_machine_v2()

# ----------------------------------------------------------------------------------------------------------------------
