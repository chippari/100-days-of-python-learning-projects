# ----------------------------------------------------------------------------------------------------------------------
# > Day 27 - Mile to Kilometers Converter Project ----------------------------------------------------------------------
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

def convert_to_km(entry, label):
    miles = float(entry.get() if entry.get() != "" else 0)
    kilometers = round(miles * 1.6)
    label.configure(text=kilometers)

# > Main ---------------------------------------------------------------------------------------------------------------

def main():
    # Window Setup.
    window = Tk()
    window.title("Mile to Km Converter")
    window.minsize(width=250, height=100)
    window.config(padx=10, pady=10)

    # Window Grid Setup.
    for i in range(3):
        window.rowconfigure(i, weight=1)
        window.columnconfigure(i, weight=1)

    # Entry Setup.
    entry = Entry(width=15)
    entry.grid(row=0, column=1, sticky="")

    # "Miles" Label Setup.
    miles_label = Label(text="Miles", font=("Arial", 10, "bold"))
    miles_label.grid(row=0, column=2, sticky="")

    # "is equal to" Label Setup.
    equal_to_label = Label(text="is equal to", font=("Arial", 10, "bold"))
    equal_to_label.grid(row=1, column=0, sticky="")

    # Result in Km Label.
    result_label = Label(text="0", font=("Arial", 10, "normal"))
    result_label.grid(row=1, column=1, sticky="")

    # "Km" Label.
    km_label = Label(text="Km", font=("Arial", 10, "bold"))
    km_label.grid(row=1, column=2, sticky="")

    # Calculate Button.
    calculate_button = Button(text="Calculate", font=("Arial", 10, "normal"), command= lambda: convert_to_km(entry, result_label))
    calculate_button.grid(row=2, column=1, sticky="")

    # Keep Window Showing on Screen.
    window.mainloop()

if __name__ == '__main__':
    main()

# ----------------------------------------------------------------------------------------------------------------------
