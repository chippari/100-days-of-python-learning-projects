# ----------------------------------------------------------------------------------------------------------------------
# > Day 30 - NATO Alphabet Project V2 ----------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# > File: main.py
# > Module: Main Module
# > Description: Entry point of the application; initializes and runs the main logic.
# > Author: Fabio Chippari
# > Created: 2025-10-22
# ----------------------------------------------------------------------------------------------------------------------
# > Imports ------------------------------------------------------------------------------------------------------------
from tkinter import Toplevel

import pandas as pd

# > Main ---------------------------------------------------------------------------------------------------------------

def main():
    nato_data = pd.read_csv("nato_phonetic_alphabet.csv")
    nato_dict = {row.letter: row.code for (index, row) in nato_data.iterrows()}

    while True:
        user_input = input("Enter a word: ").upper()
        try:
            nato_output = [nato_dict[letter] for letter in user_input]
        except KeyError:
            print("Sorry, only letters in the alphabet are allowed.")
        else:
            print(nato_output)
            break

if __name__ == "__main__":
    main()

# ----------------------------------------------------------------------------------------------------------------------
