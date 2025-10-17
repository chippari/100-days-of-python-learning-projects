# ----------------------------------------------------------------------------------------------------------------------
# > Day 25 - Weather Forecast Project ----------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# > File: main.py
# > Module: Main Module
# > Description: Entry point of the application; initializes and runs the main logic.
# > Author: Fabio Chippari
# > Created: 2025-10-17
# ----------------------------------------------------------------------------------------------------------------------

with open(file="weather_data.csv", mode="r") as data:
    weather_data_csv = data.readlines()

weather_data = []

for line in weather_data_csv:
    stripped_line = line.strip("\n")
    split_line = stripped_line.split(",")
    weather_data.append(split_line)

day = weather_data[0][0]
temperature = weather_data[0][1]
condition = weather_data[0][2]

weather_data.remove(weather_data[0])

user_input = input("Enter a day of weather forecast: ")

for day in weather_data:
    if user_input == weather_data[day - 1]:
        print(day)


# ----------------------------------------------------------------------------------------------------------------------