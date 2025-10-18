# ----------------------------------------------------------------------------------------------------------------------
# > Day 26 - Learning about List Comprehension -------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# > File: main.py
# > Module: Main Module
# > Description: Entry point of the application; initializes and runs the main logic.
# > Author: Fabio Chippari
# > Created: 2025-10-18
# ----------------------------------------------------------------------------------------------------------------------
# > 1. List Comprehension ----------------------------------------------------------------------------------------------
print("\n> 1. List Comprehension")

# Structure of List Comprehension:
# new_list = [new_item for item in list]

# Example 1:
numbers = [1, 2, 3]
new_numbers = [num + 1 for num in numbers]

print("Example 1:")
print(f" Before: {numbers} \n After: {new_numbers}")

# Example 2:
name = "Fabio"
letters = [letter for letter in name]

print("\nExample 2:")
print(f" Before: {name} \n After: {letters}")

# Example 3:
num_range_double = [num * 2 for num in range(1, 5)]

print("\nExample 3:")
print(f" After: {num_range_double}")

# > 2. Conditional List Comprehension ----------------------------------------------------------------------------------
print("\n> 2. Conditional List Comprehension")

# Structure of Conditional List Comprehension:
# new_list = [new_item for item in list if condition]

# Example 1:
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]

print("Example 1:")
print(f" Before: {names} \n After: {short_names}")

# Example 2:
long_names = [name.upper() for name in names if len(name) > 5]

print("\nExample 2:")
print(f" Before: {names} \n After: {long_names}")

# ----------------------------------------------------------------------------------------------------------------------
