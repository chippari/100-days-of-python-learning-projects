# ----------------------------------------------------------------------------------------------------------------------
# > Day 28 - Pomodoro Application Project ------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# > File: main.py
# > Module: Main Module
# > Description: Entry point of the application; initializes and runs the main logic.
# > Author: Fabio Chippari
# > Created: 2025-10-20
# ----------------------------------------------------------------------------------------------------------------------
# > Imports ------------------------------------------------------------------------------------------------------------

from tkinter import *
import math

# > Constants / Configuration ------------------------------------------------------------------------------------------

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0

# > Functions ----------------------------------------------------------------------------------------------------------
# Timer Mechanism Setup.
def start_timer(window, canvas, timer_text, timer_label):
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # If it's the 1st/3rd/5th/7th rep:
    if reps % 2 != 0:
        timer_label.config(text="Work", fg=GREEN)
        count_down(window, canvas, timer_text, timer_label, 10)
    # If it's the 8th rep:
    elif reps % 8 == 0:
        timer_label.config(text="BREAK", fg=RED)
        count_down(window, canvas, timer_text, timer_label, 5)
    # If it's 2nd/4th/6th rep:
    else:
        timer_label.config(text="Break", fg=PINK)
        count_down(window, canvas, timer_text, timer_label, 3)

# # Countdown Mechanism Function.
def count_down(window, canvas, timer_text, timer_label, count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, window, canvas, timer_text, timer_label, count - 1)
    else:
        start_timer(window, canvas, timer_text, timer_label)

# > Main ---------------------------------------------------------------------------------------------------------------

def main():
    # > UI Setup -------------------------------------------------------------------------------------------------------
    # Window Setup.
    window = Tk()
    window.title("Pomodoro")
    window.minsize(width=500, height=500)
    window.resizable(width=False, height=False)
    window.config(padx=20, pady=20, bg=YELLOW)

    # Window Grid Setup (Rows & Columns).
    rows = 4
    for i in range(rows):
        window.grid_rowconfigure(i, weight=1)

    columns = 3
    for i in range(columns):
        window.grid_columnconfigure(i, weight=1)

    # Canvas Setup.
    canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
    # Canvas Image Setup.
    tomato_img = PhotoImage(file="tomato.png")
    canvas.create_image(100, 112, image=tomato_img)
    # Canvas Text Setup.
    timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 24, "bold"))
    # Canvas Grid Position.
    canvas.grid(row=1, column=1, pady=10)

    # Timer Label Setup.
    timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 32, "bold"))
    # Timer Label Grid Position.
    timer_label.grid(row=0, column=1, sticky="s", padx=20, pady=10)

    # Checkmark Label Setup.
    checkmark_label = Label(text="✔", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
    # Checkmark Label Grid Position.
    checkmark_label.grid(row=3, column=1, sticky="n", padx=20, pady=10)

    # Start Button Setup.
    start_button = Button(text="Start", font=(FONT_NAME, 14, "bold"), width=10, command= lambda: start_timer(window, canvas, timer_text, timer_label))
    start_button.grid(row=2, column=0)

    # Reset Button Setup.
    reset_button = Button(text="Reset", font=(FONT_NAME, 14, "bold"), width=10)
    reset_button.grid(row=2, column=2)

    # Keep Window Showing on Screen.
    window.mainloop()

if __name__ == '__main__':
    main()

# ----------------------------------------------------------------------------------------------------------------------
