# ----------------------------------------------------------------------------------------------------------------------
# > Day 31 - Flash Card App Project ------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# > File: main.py
# > Module: Main Module
# > Description: Entry point of the application; initializes and runs the main logic.
# > Author: Fabio Chippari
# > Created: 2025-10-22
# ----------------------------------------------------------------------------------------------------------------------
# > Imports ------------------------------------------------------------------------------------------------------------

import random
import pandas
from tkinter import *
from typing import Optional

# > Constants / Configuration ------------------------------------------------------------------------------------------

FONT = "Arial"
BACKGROUND_COLOR = "#B1DDC6"
LEARN_LANG = "Portuguese"
NATIVE_LANG = "English"

# > Global Variables ---------------------------------------------------------------------------------------------------

window: Optional[Tk] = None
canvas: Optional[Canvas] = None
card_language: Optional[str] = None
card_word: Optional[str] = None

# > Functions ----------------------------------------------------------------------------------------------------------
# >> Generate Random Word ----------------------------------------------------------------------------------------------
def next_card():
    # Get Access from CSV File using Pandas and Transform in Dictionary.
    data = pandas.read_csv("data/portuguese_words.csv")
    words_dict = data.to_dict(orient="records")

    # Get a random word on the two languages and save word in language to Learn.
    word_chosen = random.choice(words_dict)
    word_to_learn = word_chosen[LEARN_LANG]

    # Change Card Language and Card Word Text.
    canvas.itemconfig(card_language, text=LEARN_LANG)
    canvas.itemconfig(card_word, text=word_to_learn)

# > Main ---------------------------------------------------------------------------------------------------------------

def main():
    # > Calling Global Variables ---------------------------------------------------------------------------------------
    global window, canvas, card_language, card_word

    # > UI Setup -------------------------------------------------------------------------------------------------------

    # Window Setup.
    window = Tk()
    window.title("Flash Card App")
    window.minsize(900, 750)
    window.config(background=BACKGROUND_COLOR, padx=50, pady=50)

    # Window Grid Setup (Rows & Columns)
    rows_and_columns = 2
    for i in range(rows_and_columns):
        window.rowconfigure(i, weight=1)
        window.columnconfigure(i, weight=1)

    # Canvas Setup.
    canvas = Canvas(width=800, height=530, bg=BACKGROUND_COLOR, highlightthickness=0)
    # Canvas Front Card Setup.
    front_card_img = PhotoImage(file="images/card_front.png")
    canvas.create_image(400, 265, image=front_card_img)
    # Card Language Canvas Text Setup.
    card_language = canvas.create_text(400, 150, text="", font=(FONT, 40, "italic"))
    # Word Card Canvas Text Setup.
    card_word = canvas.create_text(400, 265, text="", font=(FONT, 60, "bold"))
    # Canvas Grid Position Setup.
    canvas.grid(row=0, column=0, columnspan=2)

    # Wrong Button Setup.
    wrong_img = PhotoImage(file="images/wrong.png")
    wrong_button = Button(image=wrong_img, bg=BACKGROUND_COLOR, activebackground=BACKGROUND_COLOR, bd=0, command=next_card)
    wrong_button.grid(row=1, column=0)

    # Right Button Setup.
    right_img = PhotoImage(file="images/right.png")
    right_button = Button(image=right_img, bg=BACKGROUND_COLOR, activebackground=BACKGROUND_COLOR, bd=0, command=next_card)
    right_button.grid(row=1, column=1)

    # Calling Next Card Word to Set Initial Language and Word on Card.
    next_card()

    # Window Mainloop.
    window.mainloop()

if __name__ == '__main__':
    main()

# ----------------------------------------------------------------------------------------------------------------------
