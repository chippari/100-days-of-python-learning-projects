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

# Player Object.
player = Player()

# Screen Listen.
screen.listen()
# Player Movement with Keywords.
screen.onkey(key="Up", fun=player.move_up)
screen.onkey(key="Down", fun=player.move_down)
screen.onkey(key="Left", fun=player.move_left)
screen.onkey(key="Right", fun=player.move_right)

# ScoreBoard Object.
scoreboard = Scoreboard()

car = CarManager()

# Capstone Game Loop.
game_is_on = True
while game_is_on:
    # Set Time Delay to Screen Update.
    time.sleep(0.01)
    # Screen Update.
    screen.update()

    # If Player arrives at top, reset its position.
    if player.ycor() > 280:
        scoreboard.increase_level()
        player.reset_position()

# Screen Exit on Click.
screen.exitonclick()

# ----------------------------------------------------------------------------------------------------------------------