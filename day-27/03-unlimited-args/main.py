# ----------------------------------------------------------------------------------------------------------------------
# > Day 27 - Learning about Unlimited Arguments ------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# > File: main.py
# > Module: Main Module
# > Description: Entry point of the application; initializes and runs the main logic.
# > Author: Fabio Chippari
# > Created: 2025-10-19
# ----------------------------------------------------------------------------------------------------------------------

# To create a Function with Unlimited Values, it needs to put the * symbol, and it's best practice to write "args".
def add(*args):
    return sum(args)

# Calling Add Function with Unlimited Values.
print(add(1,2,3,4))

# ----------------------------------------------------------------------------------------------------------------------
