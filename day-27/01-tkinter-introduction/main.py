# ----------------------------------------------------------------------------------------------------------------------
# > Day 27 - Introduction to Tkinter -----------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# > File: main.py
# > Module: Main Module
# > Description: Entry point of the application; initializes and runs the main logic.
# > Author: Fabio Chippari
# > Created: 2025-10-19
# ----------------------------------------------------------------------------------------------------------------------

import tkinter

# Setup Window.
window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label Setup
label = tkinter.Label(text="I am a Label", font=("Times New Roman", 16, "bold"))
label.pack()



# Keep Window Showing on Screen. ATTENTION: It's need to be always on the end.
window.mainloop()

# ----------------------------------------------------------------------------------------------------------------------
