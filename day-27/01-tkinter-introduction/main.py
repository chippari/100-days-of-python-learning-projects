# ----------------------------------------------------------------------------------------------------------------------
# > Day 27 - Introduction to Tkinter -----------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# > File: main.py
# > Module: Main Module
# > Description: Entry point of the application; initializes and runs the main logic.
# > Author: Fabio Chippari
# > Created: 2025-10-19
# ----------------------------------------------------------------------------------------------------------------------
# > Imports ------------------------------------------------------------------------------------------------------------

from tkinter import *

# > Functions ----------------------------------------------------------------------------------------------------------

def button_clicked(label, entry):
    new_text = entry.get()
    label.config(text=new_text)

# > Main ---------------------------------------------------------------------------------------------------------------

def main():
    # Setup Window.
    window = Tk()
    window.title("My First GUI Program")
    window.minsize(width=500, height=300)
    window.config(padx= 10, pady= 10)

    # Window Grid Setup.
    # Window Rows and Columns.
    for i in range(3):
        window.columnconfigure(i, weight=1)
        window.rowconfigure(i, weight=1)


    # Label Setup.
    label = Label(text="I am a Label", font=("Times New Roman", 16, "bold"))
    label.grid(row= 0, column= 1, sticky= "s")

    # Button Setup.
    button = Button(text="Click Me", command=lambda: button_clicked(label, entry))
    button.grid(row= 1, column= 1, sticky= "")

    # Entry Setup.
    entry = Entry(width=25)
    entry.grid(row= 2, column= 1, sticky= "n")

    # Keep Window Showing on Screen. ATTENTION: It's need to be always on the end.
    window.mainloop()

if __name__ == '__main__':
    main()

# ----------------------------------------------------------------------------------------------------------------------
