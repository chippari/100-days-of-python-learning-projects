# > Day 23 -------------------------------------------------------------------------------------------------------------
# > 1. Main Module - Capstone Game Project -----------------------------------------------------------------------------

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from draw_line import DrawLine

# Screen Object.
screen = Screen()

# Screen Setup.
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Capstone Game Project")

# Screen Tracer to track animation.
screen.tracer(0)

# Draw Line Object.
draw_line = DrawLine()
# Draw Start Line & Finish Line (Just Visual).
draw_line.start_line()
draw_line.finish_line()

# ScoreBoard Object.
scoreboard = Scoreboard()

# Player Object.
player = Player()

# Screen Listen.
screen.listen()
# Player Movement with Keywords.
screen.onkey(key="Up", fun=player.move_up)
screen.onkey(key="Down", fun=player.move_down)
screen.onkey(key="Left", fun=player.move_left)
screen.onkey(key="Right", fun=player.move_right)

# Car Object.
car_manager = CarManager()

# Capstone Game Loop.
game_is_on = True
while game_is_on:
    # Set Time Delay to Screen Update.
    time.sleep(0.05)
    # Screen Update.
    screen.update()

    # Create Cars & Move them.
    car_manager.create_car()
    car_manager.move_cars()

    # Detect Collision with Car.
    for car in car_manager.cars:
        if car.distance(player) < 30:
            game_is_on = False
            scoreboard.game_over()

    # Detect when Player cross completely.
    if player.ycor() > 280:
        scoreboard.increase_level()
        player.reset_position()
        car_manager.reset_cars()

# Screen Exit on Click.
screen.exitonclick()

# ----------------------------------------------------------------------------------------------------------------------