# > Day 19 -------------------------------------------------------------------------------------------------------------
# > 1. Etch A Sketch Project -------------------------------------------------------------------------------------------

from turtle import Turtle, Screen

# Turtle and Screen Objects
bob = Turtle()
screen = Screen()

def move_forward():
    bob.forward(10)

def move_backward():
    bob.backward(10)

def turn_left():
    bob.left(10)

def turn_right():
    bob.right(10)

def clear():
    bob.clear()
    bob.penup()
    bob.home()
    bob.pendown()

bob.pensize(2)

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear)

screen.exitonclick()

# ----------------------------------------------------------------------------------------------------------------------