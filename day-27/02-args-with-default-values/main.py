# ----------------------------------------------------------------------------------------------------------------------
# > Day 27 - Learning about Arguments with Default Values --------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# > File: main.py
# > Module: Main Module
# > Description: Entry point of the application; initializes and runs the main logic.
# > Author: Fabio Chippari
# > Created: 2025-10-19
# ----------------------------------------------------------------------------------------------------------------------

# Create a function with Default Values
def my_function(a = 1, b = 2, c = 3):
    print(a, b, c)

# Calling my_function without passing any values, so it will return with default values.
my_function()

# If you call my_function with some value, it will return with all set values or with some set values and default values.
my_function(a = 10)

# ----------------------------------------------------------------------------------------------------------------------
