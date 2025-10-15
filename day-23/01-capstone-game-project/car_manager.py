# > Day 23 -------------------------------------------------------------------------------------------------------------
# > 1. Car Manager Module - Capstone Game Project ----------------------------------------------------------------------

from turtle import Turtle
from random import randint, choice

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
LIMIT_AREA_X = 300
LIMIT_AREA_Y_POSITIVE = 240
LIMIT_AREA_Y_NEGATIVE =  190

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shapesize(stretch_wid=1.5, stretch_len=3.5)
        self.shape("square")
        self.color(choice(COLORS))
        self.penup()
        self.goto(0, -190)

# ----------------------------------------------------------------------------------------------------------------------