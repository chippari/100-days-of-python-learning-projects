# > Day 18 -------------------------------------------------------------------------------------------------------------
# > 1. Turtle Graphics & GUI Project -----------------------------------------------------------------------------------

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


draw_shapes = {"triangle": {"sides": 3, "color": "cyan"},
               "square": {"sides": 4, "color": "deepskyblue"},
               "pentagon": {"sides": 5, "color": "chartreuse"},
               "hexagon": {"sides": 6, "color": "yellow"},
               "heptagon": {"sides": 7, "color": "magenta"},
               "octagon": {"sides": 8, "color": "red"},
               "nonagonon": {"sides": 9, "color": "violet"},
               "decagonon": {"sides": 10, "color": "chocolate"}
}

bob.hideturtle()

for shape in draw_shapes:
    bob.pencolor(draw_shapes[shape]["color"])
    for line in range(draw_shapes[shape]["sides"]):
        bob.forward(100)
        bob.right(360 / draw_shapes[shape]["sides"])

screen = Screen()
screen.exitonclick()

# ----------------------------------------------------------------------------------------------------------------------
