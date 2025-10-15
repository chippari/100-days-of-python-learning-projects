# > Day 23 -------------------------------------------------------------------------------------------------------------
# > 1. Main Module - Capstone Game Project -----------------------------------------------------------------------------

import time
from turtle import Screen

# Screen Object.
screen = Screen()

# Screen Setup.
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Capstone Game Project")

# Screen Tracer to Animate it.
screen.tracer(0)

# Capstone Game Loop.
game_is_on = True
while game_is_on:
    # Set Time Delay to Screen Update.
    time.sleep(0.1)
    # Screen Update.
    screen.update()


# Screen Exit on Click.
screen.exitonclick()

# ----------------------------------------------------------------------------------------------------------------------