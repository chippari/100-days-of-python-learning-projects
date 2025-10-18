# ----------------------------------------------------------------------------------------------------------------------
# > Day 25 - Weather Forecast Project ----------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# > File: main.py
# > Module: Main Module
# > Description: Entry point of the application; initializes and runs the main logic.
# > Author: Fabio Chippari
# > Created: 2025-10-17
# ----------------------------------------------------------------------------------------------------------------------

# > 1. Get Weather Data using CSV Module -------------------------------------------------------------------------------

# import csv
#
# with open(file="weather_data.csv", mode="r") as data:
#     weather_data = csv.reader(data)
#     day_data = []
#     temp_data = []
#     condition_data = []
#     for row in weather_data:
#         if row[0] != "day":
#             day_data.append(row[0])
#         if row[1] != "temp":
#             temp_data.append(int(row[1]))
#         if row[2] != "condition":
#             condition_data.append(row[2])

# > 2. Get Weather Data using Pandas Library ---------------------------------------------------------------------------

import pandas

# Get and Read CSV File using pandas.
weather_data = pandas.read_csv("weather_data.csv")

# Print Specific Column, like "temp"
print(weather_data["temp"])

# ----------------------------------------------------------------------------------------------------------------------