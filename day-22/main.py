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

# Screen Tracer to track animation.
screen.tracer(0)

# Player Paddle 1 & 2 Setup.
player_paddle_1 = PlayerPaddle(pos_x=350)
player_paddle_2 = PlayerPaddle(pos_x=-350)

# Screen Listen.
screen.listen()
# Player Paddle 1 - Keywords to move UP and DOWN.
screen.onkey(key="Up", fun=player_paddle_1.up)
screen.onkey(key="Down", fun=player_paddle_1.down)
# Player Paddle 2 - Keywords to move UP and DOWN.
screen.onkey(key="w", fun=player_paddle_2.up)
screen.onkey(key="s", fun=player_paddle_2.down)

# Pong Game Loop
game_is_on = True
while game_is_on:
    screen.update()

# Screen Exit on Click - It's need to stay at bottom of code.
screen.exitonclick()

# ----------------------------------------------------------------------------------------------------------------------