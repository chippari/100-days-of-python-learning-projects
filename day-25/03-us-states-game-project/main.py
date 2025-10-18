# ----------------------------------------------------------------------------------------------------------------------
# > Day 25 - U.S. States Game Project ----------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# > File: main.py
# > Module: Main Module
# > Description: Entry point of the application; initializes and runs the main logic.
# > Author: Fabio Chippari
# > Created: 2025-10-18
# ----------------------------------------------------------------------------------------------------------------------

import turtle, pandas

# Screen Setup.
screen = turtle.Screen()
screen.setup(width=725, height=490)
screen.title("U.S. States Game")
screen.tracer(0)

# Set Image on Turtle Screen.
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")

# Turtle Setup.
text = turtle.Turtle()
text.hideturtle()
text.penup()
text.color("black")

# Get 50 States Data
states_data = pandas.read_csv("50_states.csv")

# States Guessed Variable.
states_guessed = []
states_guessed_count = 0

game_is_on = True
while game_is_on:
    # Screen Update.
    screen.update()

    # Display a Window to ask and Store it in a Variable.
    user_guess = screen.textinput(title=f"Guess the States {states_guessed_count}/50", prompt="What's another state's name?").title()

    # States Guess Loop, if is correct show on Screen and increase states_guessed.
    for state_name in states_data.state:
        if state_name == user_guess:
            name = state_name
            pos_x = states_data[states_data.state == state_name].x.values[0]
            pos_y = states_data[states_data.state == state_name].y.values[0]

            text.goto(pos_x, pos_y)
            text.write(f"{name}", align="center", font=("Arial", 8, "bold"))

            states_guessed.append(state_name)
            states_guessed_count += 1

    if user_guess == "Exit":
        game_is_on = False

    if states_guessed_count == 50:
        game_is_on = False

# If User didn't guess all 50 states.
if states_guessed_count != 50:
    # Create CSV File to Show States that weren't guessed by User.
    # 1. Create States Not Guessed List.
    states_not_guessed = []

    # 2. Loop trough States Name in States Data, and if it weren't guessed by User, append to States Not Guessed List.
    for state_name in states_data.state:
        if state_name not in states_guessed:
            states_not_guessed.append(state_name)

    # 3. Create States Not Guessed Dictionary with States Names that weren't guessed.
    states_not_guessed_dict = {
        "State": states_not_guessed
    }

    # 4. Create a States Data Frame with States Not Guessed Dictionary and Convert it to a new CSV File.
    states_df = pandas.DataFrame(states_not_guessed_dict)
    states_df.to_csv("states_not_guessed.csv")

# ----------------------------------------------------------------------------------------------------------------------