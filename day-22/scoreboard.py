# > Day 22 -------------------------------------------------------------------------------------------------------------
# > 1. Score Board Module - Pong Game Project --------------------------------------------------------------------------

from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.score_player_1 = 0
        self.score_player_2 = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(100, 220)
        self.write(self.score_player_1, align="center", font=("Arial", 44, "normal"))
        self.goto(-100, 220)
        self.write(self.score_player_2, align="center", font=("Arial", 44, "normal"))

    def point_player_1(self):
        self.score_player_1 += 1
        self.update_scoreboard()

    def point_player_2(self):
        self.score_player_2 += 1
        self.update_scoreboard()

# ----------------------------------------------------------------------------------------------------------------------