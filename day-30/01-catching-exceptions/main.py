# ----------------------------------------------------------------------------------------------------------------------
# > Day 30 - Learning about Catching Exceptions ------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# > File: main.py
# > Module: Main Module
# > Description: Entry point of the application; initializes and runs the main logic.
# > Author: Fabio Chippari
# > Created: 2025-10-22
# ----------------------------------------------------------------------------------------------------------------------
# > Common Errors ------------------------------------------------------------------------------------------------------

# >> FileNotFoundError
# with open("non_existent_file.txt", "r") as file:
#     file.read()

# >> KeyError
# ex_dict = {"key": "value"}
# value = non_dict["non_existent_key"]

# >> IndexError
# fruit_list = ["banana", "apple"]
# fruit = fruit_list[3]

# >> TypeError
# text = "abc"
# print(text + 5)

# > Catching Errors ----------------------------------------------------------------------------------------------------

# >> "try": This block contains the code that might potentially raise an exception.
try:
    # Code that might raise an exception
    result = 10 / 0
    print(result)

# >> "except": This block is executed if an exception occurs in the try block.
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

# >> "else": This block is executed only if the try block completes without raising any exceptions.
else:
    print("Operation successful!")

# >> "finally": This block is always executed, regardless of whether an exception occurred or not.
finally:
    print("Execution of the try-except block is complete.")

# ----------------------------------------------------------------------------------------------------------------------
