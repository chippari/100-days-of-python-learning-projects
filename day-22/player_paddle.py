# > Day 22 -------------------------------------------------------------------------------------------------------------
# > 1. Player Paddle - Pong Game Project -------------------------------------------------------------------------------

from turtle import Turtle

# Player Paddle Constant Variables.
UP = 90
DOWN = 270

class PlayerPaddle(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.left(90)
        self.color("white")
        self.goto(x=350, y=0)

    def move(self):
        self.forward(10)

    def up(self):
        self.setheading(UP)

    def down(self):
        self.setheading(DOWN)

# ----------------------------------------------------------------------------------------------------------------------