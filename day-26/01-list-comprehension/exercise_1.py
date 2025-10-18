# ----------------------------------------------------------------------------------------------------------------------
# > Day 26 - List Comprehension Exercise 1 -----------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# > File: exercise_1.py
# > Module: Exercise 1 Module
# > Description: Exercise 1 about List Comprehension.
# > Author: Fabio Chippari
# > Created: 2025-10-18
# ----------------------------------------------------------------------------------------------------------------------
# > [Exercise 1] Question ----------------------------------------------------------------------------------------------

# TODO: Squaring Numbers
# You are going to write a List Comprehension to create a new list called squared_numbers. This new list should contain
# every number in the list numbers but each number should be squared.
#
# E.g: 4 * 4 = 16 -> 4 squared equals 16.
# [DO NOT] modify the List numbers directly. Try to use List Comprehension instead of a Loop.
#
# Target Output:
# [1, 1, 4, 9, 25, 64, 169, 441, 1156, 3025]

# > [Exercise 1] Solution ----------------------------------------------------------------------------------------------

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [(num * num) for num in numbers]
print(squared_numbers)

# ----------------------------------------------------------------------------------------------------------------------