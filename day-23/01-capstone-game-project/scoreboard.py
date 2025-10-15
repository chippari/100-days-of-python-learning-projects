# > Day 23 -------------------------------------------------------------------------------------------------------------
# > 1. Score Board Module - Capstone Game Project ----------------------------------------------------------------------

from turtle import Turtle

# Constant Scoreboard Variables
FONT = ("Times New Roman", 16, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("black")
        self.penup()
        self.level_score = 0
        self.goto(-290, 270)
        self.update_level()

    def update_level(self):
        self.clear()
        self.write(arg=f"Level: {self.level_score}", align="left", font=FONT)

    def increase_level(self):
        self.level_score += 1
        self.update_level()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)

# ----------------------------------------------------------------------------------------------------------------------