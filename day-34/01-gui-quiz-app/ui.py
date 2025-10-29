# ----------------------------------------------------------------------------------------------------------------------
# > Day 34 - GUI Quiz App Project --------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# > File: ui.py
# > Module: UI Module
# > Description:
# > Author: Fabio Chippari
# > Created: 2025-10-27
# ----------------------------------------------------------------------------------------------------------------------
# > Imports ------------------------------------------------------------------------------------------------------------

from tkinter import *
from quiz_brain import QuizBrain

# > Constants / Configuration ------------------------------------------------------------------------------------------

THEME_COLOR = "#375362"

# > Quiz Interface Class -----------------------------------------------------------------------------------------------

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        # Get Quiz Brain.
        self.quiz = quiz_brain

        # Window Setup.
        self.window = Tk()
        self.window.title("Quiz App Project")
        self.window.minsize(width=450, height=600)
        # self.window.resizable(width=False, height=False)
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        # Window Grid Setup (Rows & Columns).
        rows = 3
        for row in range(rows):
            self.window.rowconfigure(row, weight=1)
        columns = 2
        for column in range(columns):
            self.window.columnconfigure(column, weight=1)

        # Score Label Setup.
        self.score_label = Label(text="Score: 0", font=("Arial", 12, "bold"), bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=0, columnspan=2)

        # Canvas Setup.
        self.canvas = Canvas(width=300, height=250, background="white")
        # Canvas Text.
        self.question_text = self.canvas.create_text(150, 125, width=280, text="Hello", font=("Arial", 18, "italic"))
        # Canvas Grid Position.
        self.canvas.grid(row=1, column=0, columnspan=2)

        # True Button Setup.
        self.true_button_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=self.true_button_img, activebackground=THEME_COLOR, bd=0, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)

        # False Button Setup.
        self.false_button_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=self.false_button_img, activebackground=THEME_COLOR, bd=0, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        # Get Next Question.
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")

        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz. Congratulations!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        is_true = self.quiz.check_answer("true")
        self.give_feedback(is_true)

    def false_pressed(self):
        is_false = self.quiz.check_answer("false")
        self.give_feedback(is_false)

    def give_feedback(self, button_pressed):
        if button_pressed:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)


# ----------------------------------------------------------------------------------------------------------------------
