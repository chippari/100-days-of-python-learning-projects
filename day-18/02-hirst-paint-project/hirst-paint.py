# > Day 18 -------------------------------------------------------------------------------------------------------------
# > 1. Hirst Spot Paint Project ----------------------------------------------------------------------------------------

# import colorgram
#
# hirst_extract = colorgram.extract('hirst-image.png', 20)
# hirst_colors = []
#
# for color in hirst_extract:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     hirst_colors.append((r, g, b))
#
# print(hirst_colors)

import random
import turtle
from turtle import Turtle, Screen

turtle.colormode(255)

colors_list = [(202, 172, 108), (221, 227, 233), (237, 243, 241), (154, 181, 196), (193, 161, 177), (151, 185, 173),
               (214, 203, 114), (209, 178, 193), (161, 212, 187), (174, 188, 212), (161, 203, 215), (186, 161, 63),
               (113, 122, 185), (213, 181, 180), (198, 205, 48)]

bob = Turtle()
bob.hideturtle()
bob.penup()
bob.speed("fastest")

bob_position_x = -225
bob_position_y = -225
space_between = 54

for line in range(9):
    bob.teleport(bob_position_x, bob_position_y)
    for dot in range(9):
        random_color = random.choice(colors_list)
        bob.dot(21, random_color)
        bob.forward(space_between)

    bob_position_y += space_between

screen = Screen()
screen.exitonclick()

# ----------------------------------------------------------------------------------------------------------------------
