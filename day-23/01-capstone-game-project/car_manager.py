# > Day 23 -------------------------------------------------------------------------------------------------------------
# > 1. Car Manager Module - Capstone Game Project ----------------------------------------------------------------------

from turtle import Turtle
from random import randint, choice

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 20

LIMIT_POS_X = 350
LIMIT_POS_Y =  (-180, 220)
MIN_DIST = 90

class CarManager:
    def __init__(self):
        self.cars = []

    def create_car(self):
        slow_down_creation = randint(1, 10)
        if slow_down_creation == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1.5, stretch_len=3)
            new_car.color(choice(COLORS))
            new_car.penup()
            pos_x = LIMIT_POS_X
            pos_y = randint(LIMIT_POS_Y[0], LIMIT_POS_Y[1])
            new_car.goto(pos_x, pos_y)
            self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.backward(STARTING_MOVE_DISTANCE)

    def reset_cars(self):
        for car in self.cars:
            pos_x = -LIMIT_POS_X
            pos_y = randint(LIMIT_POS_Y[0], LIMIT_POS_Y[1])
            car.goto(pos_x, pos_y)

# ----------------------------------------------------------------------------------------------------------------------