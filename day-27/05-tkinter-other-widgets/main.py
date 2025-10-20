# ----------------------------------------------------------------------------------------------------------------------
# > Day 27 - Tkinter Other Widgets -------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# > File: main.py
# > Module: Main Module
# > Description: Entry point of the application; initializes and runs the main logic.
# > Author: Fabio Chippari
# > Created: 2025-10-20
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
    window.title("Other Tkinter Widgets Examples")
    window.minsize(width=350, height=500)

    # Label Setup.
    label = Label(text="I am a Label", font=("Times New Roman", 16, "bold"))
    label.pack()

    # Button Setup.
    button = Button(text="Click Me", command=lambda: button_clicked(label, entry))
    button.pack()

    # Entry Setup.
    entry = Entry(width=30)
    entry.pack()

    # Text Box Setup.
    text = Text(width=30, height=5)
    # Put Cursor in Text Box.
    text.focus()
    # Add Some Text to Begin With.
    text.insert(END, "Example of multi-line text entry.")
    # Get Current Value in Text Box at Line 1, Character 0.
    print(text.get("1.0", END))
    text.pack()

    # Spin Box Setup.
    spinbox = Spinbox(from_=0, to=100, width=5)
    spinbox.pack()

    # Scale Setup.
    scale = Scale(from_=0, to=100)
    scale.pack()

    # Check Button Setup.
    # Variable to Hold on to Checked State, 0 is OFF, 1 is ON.
    checked_state = IntVar()
    checkbutton = Checkbutton(text="Is ON?", variable=checked_state)
    checkbutton.pack()

    # Radio Button Setup.
    # Variable to Hold on to Which Radio Button Value is Checked.
    radio_state = IntVar()
    radiobutton1 = Radiobutton(text="Option 1", value=1, variable=radio_state)
    radiobutton2 = Radiobutton(text="Option 2", value=2, variable=radio_state)
    radiobutton1.pack()
    radiobutton2.pack()

    # List Box Setup.
    listbox = Listbox(height=4)
    fruits = ["Apple", "Pear", "Orange", "Banana"]

    for item in fruits:
        listbox.insert(fruits.index(item), item)

    listbox.bind("<<ListboxSelect>>")
    listbox.pack()

    # Keep Window Showing on Screen. ATTENTION: It's need to be always on the end.
    window.mainloop()

if __name__ == '__main__':
    main()

# ----------------------------------------------------------------------------------------------------------------------
