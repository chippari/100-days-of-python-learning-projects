# ----------------------------------------------------------------------------------------------------------------------
# > Day 33 - Kanye Quotes App Project ----------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# > File: main.py
# > Module: Main Module
# > Description: Entry point of the application; initializes and runs the main logic.
# > Author: Fabio Chippari
# > Created: 2025-10-26
# ----------------------------------------------------------------------------------------------------------------------
# > Imports ------------------------------------------------------------------------------------------------------------

import requests
from tkinter import *

# > Functions ----------------------------------------------------------------------------------------------------------

def get_quote():
    pass
    # Write your code here.

# > Main ---------------------------------------------------------------------------------------------------------------

def main():

    # Window Setup.
    window = Tk()
    window.title("Kanye Says...")
    window.resizable(width=False, height=False)
    window.config(padx=50, pady=50)

    # Canvas Setup.
    canvas = Canvas(width=300, height=414)
    background_img = PhotoImage(file="background.png")
    canvas.create_image(150, 207, image=background_img)
    quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
    canvas.grid(row=0, column=0)

    # Button Setup.
    kanye_img = PhotoImage(file="kanye.png")
    kanye_button = Button(image=kanye_img, bd=0, command=get_quote)
    kanye_button.grid(row=1, column=0)

    window.mainloop()

if __name__ == '__main__':
    main()

# ----------------------------------------------------------------------------------------------------------------------
