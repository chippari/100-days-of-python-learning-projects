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
# try:
#     result = 10 / 0 # Code that might raise an exception
#     print(result)

# >> "except": This block is executed if an exception occurs in the try block.
# except ZeroDivisionError:
#     print("Error: Cannot divide by zero!")

# >> "else": This block is executed only if the try block completes without raising any exceptions.
# else:
#     print("Operation successful!")

# >> "finally": This block is always executed, regardless of whether an exception occurred or not.
# finally:
#     print("Execution of the try-except block is complete.")

# > Raising Exceptions -------------------------------------------------------------------------------------------------

# >> "raise": is used to explicitly trigger an exception, such as ValueError, TypeError, NameError, etc.

# height = float(input("(Centimeters) Height: "))
# weight = float(input("(Kilograms) Weight: "))
#
# if height > 240:
#     raise ValueError("Human Height should not be over 240 centimeters.")
#
# bmi = round(weight / (height / 100) ** 2, 1)
# print(bmi)

# > Exercise 1 ---------------------------------------------------------------------------------------------------------
print("\nExercise 1:")

# TODO: IndexError Handling
#
# Issue:
# We've got some buggy code. Try running the code. The code will crash and give you an IndexError.
# This is because we're looking through the list of fruits for an index that is out of range.
#
# Objective:
# Use what you've learnt about exception handling to prevent the program from crashing. If the user enters something
# that is out of range just print a default output of "Fruit pie".
#
# IMPORTANT: The exception handling should NOT allow each fruit to be printed when there is an exception. e.g. it
# should not print out Apple pie, Pear pie and Orange pie, when there is an exception it should only print "Fruit pie".

# Solution:
fruits = ["Apple", "Pear", "Orange"]

# Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    try:
        fruit = fruits[index]
        print(fruit + " pie")
    except IndexError:
        print("Fruit pie")

make_pie(4)

# > Exercise 2 ---------------------------------------------------------------------------------------------------------
print("\nExercise 2:")

# TODO: KeyError Handling
# We've got some buggy code, try running the code. The code will crash and give you a KeyError.
# This is because some of the posts in the facebook_posts don't have any "Likes".
#
# Objective: Use what you've learnt about exception handling to prevent the program from crashing.

# Solution:
facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]

def count_likes(posts):
    total_likes = 0
    for post in posts:
        try:
            total_likes = total_likes + post['Likes']
        except KeyError:
            pass

    return total_likes

print(count_likes(facebook_posts))

# ----------------------------------------------------------------------------------------------------------------------
