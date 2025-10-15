# > Day 22 -------------------------------------------------------------------------------------------------------------
# > 1. Player Paddle Module - Pong Game Project ------------------------------------------------------------------------

from turtle import Turtle

SCREEN_LIMIT_Y_POSITIVE = 250
SCREEN_LIMIT_Y_NEGATIVE = -250

class PlayerPaddle(Turtle):
    def __init__(self, pos_x):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(x=pos_x, y=0)

    def up(self):
        if self.ycor() < SCREEN_LIMIT_Y_POSITIVE:
            new_y = self.ycor() + 50
            self.goto(self.xcor(), new_y)

    def down(self):
        if self.ycor() > SCREEN_LIMIT_Y_NEGATIVE:
            new_y = self.ycor() - 50
            self.goto(self.xcor(), new_y)

# ----------------------------------------------------------------------------------------------------------------------