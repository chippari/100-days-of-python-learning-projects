# ----------------------------------------------------------------------------------------------------------------------
# > Day 29 - Password Manager Project ----------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# > File: main.py
# > Module: Main Module
# > Description: Entry point of the application; initializes and runs the main logic.
# > Author: Fabio Chippari
# > Created: 2025-10-21
# ----------------------------------------------------------------------------------------------------------------------
# > Imports ------------------------------------------------------------------------------------------------------------

from tkinter import *
from typing import Optional

# > Constants / Configuration ------------------------------------------------------------------------------------------

FONT = "Arial"
FONT_COLOR = "#000000"

# > Global Variables ---------------------------------------------------------------------------------------------------

window: Optional[Tk] = None
canvas: Optional[Canvas] = None

# > Functions ----------------------------------------------------------------------------------------------------------
# >> Password Generator ------------------------------------------------------------------------------------------------
# >> Save Password -----------------------------------------------------------------------------------------------------
# > Main ---------------------------------------------------------------------------------------------------------------

def main():
    # > Calling Global Variables ---------------------------------------------------------------------------------------
    global window, canvas
    # > UI Setup -------------------------------------------------------------------------------------------------------
    # Window Setup.
    window = Tk()
    window.title("Password Manager")
    window.minsize(width=550, height=400)
    window.resizable(width=False, height=False)
    window.config(padx=20, pady=20)

    # Window Grip Setup (Rows & Columns).
    rows = 5
    for i in range(rows):
        window.rowconfigure(i, weight=1)

    columns = 3
    for i in range(columns):
        window.columnconfigure(i, weight=1)

    # Canvas Setup.
    canvas = Canvas(width=200, height=200, highlightthickness=0)
    # Canvas Image Setup.
    logo_img = PhotoImage(file="logo.png")
    canvas.create_image(100, 100, image=logo_img)
    canvas.grid(row=0, column=1, sticky="nswe")

    # Website Label Setup.
    website_label = Label(text="Website:", fg=FONT_COLOR, font=(FONT, 12, "normal"))
    website_label.grid(row=1, column=0, sticky="e")

    # Website Entry Setup.
    website_entry = Entry(font=(FONT, 14, "normal"))
    website_entry.grid(row=1, column=1, columnspan=2, sticky="we", pady=10)

    # Email / Username Label Setup.
    email_label = Label(text="Email / Username:", fg=FONT_COLOR, font=(FONT, 12, "normal"))
    email_label.grid(row=2, column=0, sticky="e")

    # Email / Username Entry Setup.
    email_entry = Entry(font=(FONT, 14, "normal"))
    email_entry.grid(row=2, column=1, columnspan=2, sticky="we")

    # Password Label Setup.
    password_label = Label(text="Password:", fg=FONT_COLOR, font=(FONT, 12, "normal"))
    password_label.grid(row=3, column=0, sticky="e")

    # Password Entry Setup.
    password_entry = Entry(font=(FONT, 14, "normal"))
    password_entry.grid(row=3, column=1, sticky="we", pady=10)

    # Generate Password Button Setup.
    generate_button = Button(text="Generate", fg=FONT_COLOR, font=(FONT, 10, "bold"))
    generate_button.grid(row=3, column=2, sticky="we")

    # Save Password Button Setup.
    save_button = Button(text="Save Password", fg=FONT_COLOR, font=(FONT, 10, "bold"))
    save_button.grid(row=4, column=1, columnspan=2, sticky="we")


    # Keep Window Showing on Screen.
    window.mainloop()

if __name__ == '__main__':
    main()

# ----------------------------------------------------------------------------------------------------------------------
