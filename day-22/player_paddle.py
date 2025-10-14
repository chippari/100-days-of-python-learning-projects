# > Day 22 -------------------------------------------------------------------------------------------------------------
# > 1. Player Paddle Module - Pong Game Project ------------------------------------------------------------------------

from turtle import Turtle

class PlayerPaddle(Turtle):
    def __init__(self, pos_x):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(x=pos_x, y=0)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

# ----------------------------------------------------------------------------------------------------------------------