# > Day 23 -------------------------------------------------------------------------------------------------------------
# > 1. Player Module - Capstone Game Project ---------------------------------------------------------------------------

from turtle import Turtle

# Constant Player Variables.
STARTING_POSITION = (0, -240)
MOVE_DISTANCE = 20
FINISH_LINE_Y = 280
LIMIT_AREA_X = 260
LIMIT_AREA_Y = 260

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shapesize(stretch_wid=1.5, stretch_len=1.5)
        self.shape("turtle")
        self.color("chartreuse")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)
        self.move_distance = MOVE_DISTANCE

    def move_up(self):
        self.setheading(90)
        self.goto(self.xcor(), self.ycor() + self.move_distance)

    def move_down(self):
        if self.ycor() > -LIMIT_AREA_Y:
            self.setheading(270)
            self.goto(self.xcor(), self.ycor() - self.move_distance)

    def move_left(self):
        if self.xcor() > -LIMIT_AREA_X:
            self.setheading(180)
            self.goto(self.xcor() - self.move_distance, self.ycor())

    def move_right(self):
        if self.xcor() < LIMIT_AREA_X:
            self.setheading(0)
            self.goto(self.xcor() + self.move_distance, self.ycor())

    def reset_position(self):
        if self.ycor() > FINISH_LINE_Y:
            self.goto(STARTING_POSITION)

# ----------------------------------------------------------------------------------------------------------------------