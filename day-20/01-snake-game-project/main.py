# > Day 20 -------------------------------------------------------------------------------------------------------------
# > 1. Main.py - Snake Game Project ---------------------------------------------------------------------------------------

from snake import Snake
from turtle import Screen
import time

# Screen Object
screen = Screen()

# Screen Settings
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

# Screen Exit on Click
screen.exitonclick()

# ----------------------------------------------------------------------------------------------------------------------