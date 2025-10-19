# ----------------------------------------------------------------------------------------------------------------------
# > Day 26 - Dictionary Comprehension Exercise 2 -----------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# > File: exercise_2.py
# > Module: Exercise 2 Module
# > Description: Exercise 2 about Dictionary Comprehension.
# > Author: Fabio Chippari
# > Created: 2025-10-19
# ----------------------------------------------------------------------------------------------------------------------
# > [Exercise 2] Question ----------------------------------------------------------------------------------------------

# TODO: Dictionary Comprehension 2
# You are going to use Dictionary Comprehension to create a dictionary called weather_f that takes each temperature in
# degrees Celsius and converts it into degrees Fahrenheit.
#
# To convert temp_c into temp_f use this formula:
# (temp_c * 9/5) + 32 = temp_f

# > [Exercise 2] Solution ----------------------------------------------------------------------------------------------

weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

weather_f = {day: ((temp_c * 9/5) + 32) for day, temp_c in weather_c.items()}
print(weather_f)

# ----------------------------------------------------------------------------------------------------------------------
