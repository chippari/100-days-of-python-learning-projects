# ----------------------------------------------------------------------------------------------------------------------
# > Day 26 - Dictionary Comprehension Exercise 1 -----------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# > File: exercise_1.py
# > Module: Exercise 1 Module
# > Description: Exercise 1 about Dictionary Comprehension.
# > Author: Fabio Chippari
# > Created: 2025-10-19
# ----------------------------------------------------------------------------------------------------------------------
# > [Exercise 1] Question ----------------------------------------------------------------------------------------------

# TODO: Dictionary Comprehension 1
# You are going to use Dictionary Comprehension to create a dictionary called result that takes each word in the given
# sentence and calculates the number of letters in each word.
# Try Googling to find out how to convert a sentence into a list of words.
#
# [Do NOT] Create a dictionary directly.
# Try to use Dictionary Comprehension instead of a Loop.
# To keep this exercise simple, count any punctuation following a word with no whitespace as part of the word.
# Note that "Swallow?" therefore has a length of 8.

# > [Exercise 1] Solution ----------------------------------------------------------------------------------------------

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word: len(word) for word in sentence.split()}
print(result)

# ----------------------------------------------------------------------------------------------------------------------