# > Day 22 -------------------------------------------------------------------------------------------------------------
# > 1. Ball Module - Pong Game Project ---------------------------------------------------------------------------------

from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(x=0, y=0)

    def move(self):
        new_x = self.xcor() + 10
        new_y = self.ycor() + 10
        self.goto(new_x, new_y)

# ----------------------------------------------------------------------------------------------------------------------