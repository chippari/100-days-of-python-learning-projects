# ----------------------------------------------------------------------------------------------------------------------
# > Day 26 - Learning about Dictionary Comprehension -------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# > File: main.py
# > Module: Main Module
# > Description: Entry point of the application; initializes and runs the main logic.
# > Author: Fabio Chippari
# > Created: 2025-10-19
# ----------------------------------------------------------------------------------------------------------------------
# > 1. Dictionary Comprehension ----------------------------------------------------------------------------------------
print("\n> 1. Dictionary Comprehension")

# Structure of Dictionary Comprehension:
# new_dict = {new_key: new_value for item in list}
# new_dict = {new_key: new_value for (key, value) in dict.items()}

import random

# Example 1:
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
student_scores = {student: random.randint(0, 100) for student in names}

print("Example 1:")
print(student_scores)

# > 2. Conditional Dictionary Comprehension ----------------------------------------------------------------------------
print("\n> 2. Conditional Dictionary Comprehension")

# Structure of Conditional Dictionary Comprehension:
# new_dict = {new_key: new_value for item in list if condition}
# new_dict = {new_key: new_value for (key, value) in dict.items() if condition}

# Example 2:
passed_student = {student: score for (student, score) in student_scores.items() if score >= 50}

print("\nExample 2:")
print(passed_student)

# ----------------------------------------------------------------------------------------------------------------------