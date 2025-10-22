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

from tkinter import *
from typing import Optional

# > Constants / Configuration ------------------------------------------------------------------------------------------

FONT = "Arial"
BACKGROUND_COLOR = "#B1DDC6"

# > Global Variables ---------------------------------------------------------------------------------------------------

window: Optional[Tk] = None
canvas: Optional[Canvas] = None

# > Functions ----------------------------------------------------------------------------------------------------------

# > Main ---------------------------------------------------------------------------------------------------------------

def main():
    # > Calling Global Variables ---------------------------------------------------------------------------------------
    global window, canvas

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
    # Language Canvas Text Setup.
    canvas.create_text(400, 150, text="Title", font=(FONT, 40, "italic"))
    # Word Canvas Text Setup.
    canvas.create_text(400, 265, text="word", font=(FONT, 60, "bold"))
    # Canvas Grid Position Setup.
    canvas.grid(row=0, column=0, columnspan=2)

    # Wrong Button Setup.
    wrong_img = PhotoImage(file="images/wrong.png")
    wrong_button = Button(image=wrong_img, bg=BACKGROUND_COLOR, activebackground=BACKGROUND_COLOR, bd=0)
    wrong_button.grid(row=1, column=0)

    # Right Button Setup.
    right_img = PhotoImage(file="images/right.png")
    right_button = Button(image=right_img, bg=BACKGROUND_COLOR, activebackground=BACKGROUND_COLOR, bd=0)
    right_button.grid(row=1, column=1)

    # Window Mainloop.
    window.mainloop()

if __name__ == '__main__':
    main()

# ----------------------------------------------------------------------------------------------------------------------
