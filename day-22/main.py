# > Day 22 -------------------------------------------------------------------------------------------------------------
# > 1. Main - Pong Game Project ----------------------------------------------------------------------------------------

import time
from turtle import Screen
from player_paddle import PlayerPaddle
from ball import Ball
from scoreboard import Scoreboard

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

# Pong Ball Object.
ball = Ball()
# ball.goto(320, -70)
# print(ball.distance(player_paddle_1))
# screen.update()

# Score Board Object.
scoreboard = Scoreboard()

# Pong Game Loop
game_is_on = True
while game_is_on:
    # Delay Time to screen update.
    time.sleep(0.05)
    # Set Screen Update.
    screen.update()

    # Ball Movement Setup.
    ball.move()

    # Detect Collision with Wall and Bounce.
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect Collision with Player Paddle 1 & Player Paddle 2.
    if (320 < ball.xcor() < 340 and abs(ball.ycor() - player_paddle_1.ycor()) <= 60) or (-340 < ball.xcor() < -320 and abs(ball.ycor() - player_paddle_2.ycor()) <= 60):
        ball.bounce_x()
        # Make ball speed up each time when one of the player hit the ball.
        ball.move_speed *= 1.05

    # Detect When Player Paddle 1 Misses the Ball.
    if ball.xcor() > 400:
        ball.reset_position()
        scoreboard.point_player_2()

    # Detect When Player Paddle 2 Misses the Ball.
    if ball.xcor() < -400:
        ball.reset_position()
        scoreboard.point_player_1()


# Screen Exit on Click - It's need to stay at bottom of code.
screen.exitonclick()

# ----------------------------------------------------------------------------------------------------------------------