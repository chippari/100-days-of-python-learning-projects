# > Day 18 -------------------------------------------------------------------------------------------------------------
# > 1. Turtle Graphics & GUI Project -----------------------------------------------------------------------------------

import random
import turtle
from turtle import Turtle, Screen

bob = Turtle()

# >> 1.1. Draw a Square ------------------------------------------------------------------------------------------------
# for _ in range(4):
#     bob.forward(100)
#     bob.left(90)

# >> 1.2. Draw a Dashed Line -------------------------------------------------------------------------------------------
# for dashed_line in range(15):
#     bob.forward(10)
#     bob.penup()
#     bob.forward(10)
#     bob.pendown()

# >> 1.3. Draw a Triangle, Square, Pentagon, Hexagon, Heptagon, Octagon, Nonagon and Decagon ---------------------------

# draw_shapes = {"triangle": {"sides": 3, "color": "cyan"},
#                "square": {"sides": 4, "color": "deepskyblue"},
#                "pentagon": {"sides": 5, "color": "chartreuse"},
#                "hexagon": {"sides": 6, "color": "yellow"},
#                "heptagon": {"sides": 7, "color": "magenta"},
#                "octagon": {"sides": 8, "color": "red"},
#                "nonagon": {"sides": 9, "color": "violet"},
#                "decagon": {"sides": 10, "color": "chocolate"}
# }
#
# bob.hideturtle()
#
# for shape in draw_shapes:
#     bob.pencolor(draw_shapes[shape]["color"])
#     for line in range(draw_shapes[shape]["sides"]):
#         bob.forward(100)
#         bob.right(360 / draw_shapes[shape]["sides"])

# >> 1.4. Draw a Random Walk -------------------------------------------------------------------------------------------

# colors = ["cyan", "deepskyblue", "chartreuse", "yellow", "magenta", "red", "violet", "chocolate"]
# directions = [0, 90, 180, 270]
#
# bob.hideturtle()
# bob.pensize(12)
# bob.speed("fastest")
#
# for walk in range(100):
#     bob.pencolor(random.choice(colors))
#     bob.forward(30)
#     bob.setheading(random.choice(directions))

# >> 1.5. Python Tuples and Random RGB Colors --------------------------------------------------------------------------

# turtle.colormode(255)
#
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     generated_color = (r, g, b)
#     return generated_color
#
# directions = [0, 90, 180, 270]
#
# bob.hideturtle()
# bob.pensize(12)
# bob.speed("fastest")
#
# for walk in range(100):
#     bob.pencolor(random_color())
#     bob.forward(30)
#     bob.setheading(random.choice(directions))

# >> 1.6. Draw a Spirograph --------------------------------------------------------------------------------------------

turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    generated_color = (r, g, b)
    return generated_color

bob.speed("fastest")
turn_complete = 360
angle = 5

for i in range(int(turn_complete / angle)):
    bob.color(random_color())
    bob.left(angle)
    bob.circle(100)


screen = Screen()
screen.exitonclick()

# ----------------------------------------------------------------------------------------------------------------------
