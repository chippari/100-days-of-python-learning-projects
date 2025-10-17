# > Day 24 -------------------------------------------------------------------------------------------------------------
# > 1. Score Board Module - Snake Game Project v2 ----------------------------------------------------------------------

from turtle import Turtle

# CONFIGURATION (Constant Scoreboard Variables)
ALIGNMENT = 'center'
FONT = ("Courier", 14, "bold")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.color("white")
        self.goto(0, 275)
        self.score = 0
        with open(file='highscore_data.txt', mode='r') as highscore_data:
            self.high_score = int(highscore_data.read())
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        with open(file='highscore_data.txt', mode='r') as highscore_data:
            self.high_score = int(highscore_data.read())
        self.write(arg=f"| Score: {self.score} | High Score: {self.high_score} |", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(file='highscore_data.txt', mode='w') as highscore_data:
                highscore_data.write(f"{self.high_score}")

        self.score = 0
        self.update_scoreboard()

# ----------------------------------------------------------------------------------------------------------------------