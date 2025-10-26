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
from typing import Optional

# > Global Variables ---------------------------------------------------------------------------------------------------

canvas: Optional[Canvas] = None
quote_text: Optional[str] = None

# > Functions ----------------------------------------------------------------------------------------------------------

def get_quote():
    # Get Response from API Endpoint.
    response = requests.get(url="https://api.kanye.rest")
    # Get Data from API Response.
    data = response.json()
    kanye_quote = data["quote"]
    # Change Quote Text on Canvas.
    canvas.itemconfig(quote_text, text=kanye_quote)

# > Main ---------------------------------------------------------------------------------------------------------------

def main():
    # > Calling Global Variables ---------------------------------------------------------------------------------------
    global canvas, quote_text

    # > UI Setup -------------------------------------------------------------------------------------------------------
    # Window Setup.
    window = Tk()
    window.title("Kanye Says...")
    window.resizable(width=False, height=False)
    window.config(padx=50, pady=50)

    # Canvas Setup.
    canvas = Canvas(width=300, height=414)
    background_img = PhotoImage(file="background.png")
    canvas.create_image(150, 207, image=background_img)
    quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 18, "bold"), fill="white")
    canvas.grid(row=0, column=0)

    # Button Setup.
    kanye_img = PhotoImage(file="kanye.png")
    kanye_button = Button(image=kanye_img, bd=0, command=get_quote)
    kanye_button.grid(row=1, column=0)

    window.mainloop()

if __name__ == '__main__':
    main()

# ----------------------------------------------------------------------------------------------------------------------
