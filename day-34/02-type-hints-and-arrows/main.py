# ----------------------------------------------------------------------------------------------------------------------
# > Day 34 - Learning About Type Hints and Arrows ----------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# > File: main.py
# > Module: Main Module
# > Description: Entry point of the application; initializes and runs the main logic.
# > Author: Fabio Chippari
# > Created: 2025-10-28
# ----------------------------------------------------------------------------------------------------------------------

# ATTENTION: This is to prevent a bug in your code, but the IDE will only highlight your code but not raise an error.

# You can set a Data Type to a variable.
name: str
age: int
height: float
is_human: bool

# You can also set a Data Type inside a function and set a Data Type to a function using Arrow.
def police_check(my_age: int) -> bool:
    if my_age >= 18:
        can_drive = True
    else:
        can_drive = False

    return can_drive

if police_check(19):
    print("You may pass.")
else:
    print("Pay a fine!")

# ----------------------------------------------------------------------------------------------------------------------
