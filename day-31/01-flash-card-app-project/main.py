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

from pandas.errors import EmptyDataError

# > Constants / Configuration ------------------------------------------------------------------------------------------

TIME_MS = 3000
FONT = "Arial"
BACKGROUND_COLOR = "#B1DDC6"
LEARN_LANG = "Portuguese"
NATIVE_LANG = "English"

# > Global Variables ---------------------------------------------------------------------------------------------------

current_card = {}
word_cards = []

window: Optional[Tk] = None
canvas: Optional[Canvas] = None

card_image: Optional[str] = None
card_language: Optional[str] = None
card_word: Optional[str] = None
front_card_img: Optional[str] = None
back_card_img: Optional[str] = None
flip_timer: Optional[str] = None

# > Functions ----------------------------------------------------------------------------------------------------------
# >> Load Data ---------------------------------------------------------------------------------------------------------
def load_data():
    # Get Words Cards from Global Scope.
    global word_cards

    # Get Access from CSV File using Pandas and Transform in Dictionary.
    try:
        data = pandas.read_csv("data/words_to_learn.csv")
    except FileNotFoundError:
        original_data = pandas.read_csv("data/portuguese_words.csv")
        word_cards = original_data.to_dict(orient="records")
    except EmptyDataError:
        original_data = pandas.read_csv("data/portuguese_words.csv")
        word_cards = original_data.to_dict(orient="records")
    else:
        word_cards = data.to_dict(orient="records")

# >> Generate Random Word ----------------------------------------------------------------------------------------------
def next_card():
    # Get a random word on the two languages and save learning word in a variable.
    global current_card
    current_card = random.choice(word_cards)
    learning_word = current_card[LEARN_LANG]

    # Change Card Language and Card Word Text to Learning Language.
    canvas.itemconfig(card_language, text=LEARN_LANG, fill="black")
    canvas.itemconfig(card_word, text=learning_word, fill="black")

    # Set Front Card Image.
    canvas.itemconfig(card_image, image=front_card_img)

    # Reset Timer to Flip Card Before.
    global flip_timer
    window.after_cancel(flip_timer)

    # Flip Card after a certain delay and show native word and language.
    flip_timer = window.after(3000, flip_card)

# >> Show Word in Native Language --------------------------------------------------------------------------------------
def flip_card():
    # Get a native word from current card.
    native_word = current_card[NATIVE_LANG]

    # Change Card Language and Card Word Text to Native Language.
    canvas.itemconfig(card_language, text=NATIVE_LANG, fill="white")
    canvas.itemconfig(card_word, text=native_word, fill="white")

    # Set Back Card Image.
    canvas.itemconfig(card_image, image=back_card_img)

# >> Know Word ---------------------------------------------------------------------------------------------------------
def know_word():
    # Remove Current Card, because the user knows that word.
    word_cards.remove(current_card)
    # The Remain Words save in to a new CSV File.
    remain_words = pandas.DataFrame(word_cards)
    remain_words.to_csv("data/words_to_learn.csv", index=False)
    # Call Next Card Function.
    next_card()

# > Main ---------------------------------------------------------------------------------------------------------------

def main():
    # > Calling Global Variables ---------------------------------------------------------------------------------------
    global window, canvas, card_image, card_language, card_word, front_card_img, back_card_img, flip_timer

    # > Loading Data ---------------------------------------------------------------------------------------------------
    load_data()

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

    # Flip Card after a certain delay and show native word and language.
    flip_timer = window.after(TIME_MS, flip_card)

    # Canvas Setup.
    canvas = Canvas(width=800, height=530, bg=BACKGROUND_COLOR, highlightthickness=0)
    # Front & Back Card Image Setup.
    front_card_img = PhotoImage(file="images/card_front.png")
    back_card_img = PhotoImage(file="images/card_back.png")
    # Card Image Canvas Setup.
    card_image = canvas.create_image(400, 265)
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
    right_button = Button(image=right_img, bg=BACKGROUND_COLOR, activebackground=BACKGROUND_COLOR, bd=0, command=know_word)
    right_button.grid(row=1, column=1)

    # Calling Next Card Word to Set Initial Language and Word on Card.
    next_card()

    # Window Mainloop.
    window.mainloop()

if __name__ == '__main__':
    main()

# ----------------------------------------------------------------------------------------------------------------------
