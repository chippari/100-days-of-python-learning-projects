# > Day 22 -------------------------------------------------------------------------------------------------------------
# > 1. Main - Pong Game Project ----------------------------------------------------------------------------------------

import time
from turtle import Screen
from player_paddle import PlayerPaddle

# Screen Setup.
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game Project")
screen.tracer(0)

# Player Paddle Setup.
player_paddle = PlayerPaddle()

# Screen Listen & Keywords to move the Player Paddle.
screen.listen()
screen.onkey(key="Up", fun=player_paddle.up)
screen.onkey(key="Down", fun=player_paddle.down)

# Pong Game Loop
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.05)
    player_paddle.move()


# Screen Exit on Click - It's need to stay at bottom of code.
screen.exitonclick()

# ----------------------------------------------------------------------------------------------------------------------