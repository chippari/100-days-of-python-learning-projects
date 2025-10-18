# ----------------------------------------------------------------------------------------------------------------------
# > Day 26 - List Comprehension Exercise 3 -----------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# > File: exercise_3.py
# > Module: Exercise 3 Module
# > Description: Exercise 3 about List Comprehension.
# > Author: Fabio Chippari
# > Created: 2025-10-18
# ----------------------------------------------------------------------------------------------------------------------
# > [Exercise 3] Question ----------------------------------------------------------------------------------------------

# TODO: Data Overlap
# Take a look inside file1.txt and file2.txt. They each contain a bunch of numbers, each number on a new line.
# You are going to create a list called result which contains the numbers that are common in both files.
# e.g. if file1.txt contained:
# 1
# 2
# 3
#
# and file2.txt contained:
# 2
# 3
# 4
#
# result = [2, 3]
# IMPORTANT:  The output should be a list of integers and not strings!
# Try to use List Comprehension instead of a Loop.

# > [Exercise 3] Solution ----------------------------------------------------------------------------------------------

with open("exercise_3_file_1.txt") as f1:
    file_1_list = [line.strip() for line in f1 if line.strip()]

with open("exercise_3_file_2.txt") as f2:
    file_2_list = [line.strip() for line in f2 if line.strip()]

result = [int(num) for num in file_1_list if num in file_2_list]

print(result)

# ----------------------------------------------------------------------------------------------------------------------