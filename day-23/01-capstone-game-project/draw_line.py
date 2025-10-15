# > Day 23 -------------------------------------------------------------------------------------------------------------
# > 1. Screen Line Module - Capstone Game Project ----------------------------------------------------------------------

from turtle import Turtle

DRAW_START_POS_X = 300
DRAW_START_POS_Y = 220
DRAW_FINISH_POS_X = 300
DRAW_FINISH_POS_Y = 260

class DrawLine(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.pensize(4)
        self.hideturtle()
        self.penup()

    def start_line(self):
        self.goto(x=-DRAW_START_POS_X, y=-DRAW_START_POS_Y)
        self.pendown()
        self.goto(x=DRAW_START_POS_X, y=-DRAW_START_POS_Y)
        self.penup()

    def finish_line(self):
        self.goto(x=-DRAW_FINISH_POS_X, y=DRAW_FINISH_POS_Y)
        self.pendown()
        self.goto(x=DRAW_FINISH_POS_X, y=DRAW_FINISH_POS_Y)
        self.penup()

# ----------------------------------------------------------------------------------------------------------------------