# > Day 20 -------------------------------------------------------------------------------------------------------------
# > 1. Main - Snake Game Project ---------------------------------------------------------------------------------------

import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

# Screen Object.
screen = Screen()

# Screen Settings.
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# Snake & Food Objects.
snake = Snake()
food = Food()
score_board = ScoreBoard()

# Screen Listen Keywords to move snake.
screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

# Snake Game Loop.
game_is_on = True
while game_is_on:
    # Screen Update to happen the animation.
    screen.update()
    # Time to delay the snake animation.
    time.sleep(0.075)
    # Calling Move Method to move snake.
    snake.move()
    # Detect Collision with Food.
    if snake.head.distance(food) < 15:
        score_board.increase_score()
        food.refresh()


# Screen Exit on Click.
screen.exitonclick()

# ----------------------------------------------------------------------------------------------------------------------