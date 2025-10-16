# > Day 24 -------------------------------------------------------------------------------------------------------------
# > 1. Score Board Module - Snake Game Project v2 ----------------------------------------------------------------------

from turtle import Turtle

ALIGNMENT = 'center'
FONT = ("Courier", 14, "bold")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.color("white")
        self.goto(0, 275)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"| Score: {self.score} | High Score: {self.high_score} |", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score

        self.score = 0
        self.update_scoreboard()

# ----------------------------------------------------------------------------------------------------------------------