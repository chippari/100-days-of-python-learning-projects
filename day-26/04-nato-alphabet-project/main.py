# ----------------------------------------------------------------------------------------------------------------------
# > Day 26 - NATO Alphabet Project -------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# > File: main.py
# > Module: Main Module
# > Description: Entry point of the application; initializes and runs the main logic.
# > Author: Fabio Chippari
# > Created: 2025-10-19
# ----------------------------------------------------------------------------------------------------------------------

import pandas as pd

# TODO-1: Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}.
nato_data = pd.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in nato_data.iterrows()}

# TODO-2: Create a list comprehension of the phonetic code words from a word that the user inputs.
user_input = input("Enter a word: ").upper()
nato_output = [nato_dict[letter] for letter in user_input]
print(nato_output)

# ----------------------------------------------------------------------------------------------------------------------
