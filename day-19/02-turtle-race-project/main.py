# > Day 19 -------------------------------------------------------------------------------------------------------------
# > 1. Turtle Race Project ---------------------------------------------------------------------------------------------

import random
import turtle
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)

# User Input
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ").lower()
colors = ["red", "blue", "green", "yellow", "orange", "purple", "pink"]

turtles = []
num_of_turtles = 7
turtle_position_y = -105

for turtle in range(num_of_turtles):
    # Create Turtles, Set Colors and Set Initial Position for each.
    turtles.append(Turtle(shape="turtle"))
    turtles[turtle].color(colors[turtle])
    turtles[turtle].penup()

    turtles[turtle].goto(x=-230, y=turtle_position_y)
    turtle_position_y += 35

is_race_on = False

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in range(len(turtles)):
        rand_distance = random.randint(0, 10)
        turtles[turtle].forward(rand_distance)

        if turtles[turtle].xcor() >= 250:
            is_race_on = False

            if user_bet == colors[turtle]:
                print("You win!")
            else:
                print(f"You lose! The winner was {colors[turtle]} turtle.")

screen.exitonclick()

# ----------------------------------------------------------------------------------------------------------------------