# > Day 20 -------------------------------------------------------------------------------------------------------------
# > 1. Turtle Race Project ---------------------------------------------------------------------------------------------

from turtle import Turtle, Screen
import time

# Objects
screen = Screen()

# Screen Settings
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# Snake Settings
snake_body = []
snake_length = 3
segment_pos_x = 0
set_pos_x = -20

for segment in range(snake_length):
    # Create Snake Segments and Set Start Position for each.
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(x=segment_pos_x, y=0)

    snake_body.append(new_segment)
    segment_pos_x += set_pos_x


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    for seg_num in range(len(snake_body) - 1, 0, -1):
        new_x = snake_body[seg_num - 1].xcor()
        new_y = snake_body[seg_num - 1].ycor()
        snake_body[seg_num].goto(new_x, new_y)

    snake_body[0].forward(20)


# Screen Exit on Click
screen.exitonclick()

# ----------------------------------------------------------------------------------------------------------------------