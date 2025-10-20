# ----------------------------------------------------------------------------------------------------------------------
# > Day 27 - Learning about Unlimited Keyword Arguments ----------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# > File: main.py
# > Module: Main Module
# > Description: Entry point of the application; initializes and runs the main logic.
# > Author: Fabio Chippari
# > Created: 2025-10-19
# ----------------------------------------------------------------------------------------------------------------------

# To create a Function with Unlimited Keywords Values, it needs to put two "**" symbols,
# and it's best practice to write "kwargs".
def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    return n

result = calculate(2, add=3, multiply=5)
print(result)

# ----------------------------------------------------------------------------------------------------------------------
