# ----------------------------------------------------------------------------------------------------------------------
# > Day 26 - List Comprehension Exercise 2 -----------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# > File: exercise_2.py
# > Module: Exercise 2 Module
# > Description: Exercise 2 about List Comprehension.
# > Author: Fabio Chippari
# > Created: 2025-10-18
# ----------------------------------------------------------------------------------------------------------------------
# > [Exercise 2] Question ----------------------------------------------------------------------------------------------

# TODO: Filtering Even Numbers
# In this list comprehension exercise you will practice using list comprehension to filter out the even numbers from a
# series of numbers.
#
# First, use list comprehension to convert the list_of_strings to a list of integers called numbers.
# Then use list comprehension again to create a new list called result.
# This new list should only contain the even numbers from the list numbers.
# Again, try to use Python's List Comprehension instead of a Loop.

# > [Exercise 2] Solution ----------------------------------------------------------------------------------------------

list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers = [int(num) for num in list_of_strings]
result = [even_num for even_num in numbers if even_num % 2 == 0]
print(result)

# ----------------------------------------------------------------------------------------------------------------------