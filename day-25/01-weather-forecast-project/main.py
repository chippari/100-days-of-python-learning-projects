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

# Print Specific Column, like "temp".
# print(weather_data["temp"])

# The Most Two Important Data Structure.
# 1. Dataframe (2-dimensional labeled data structure):
# print(type(weather_data))

# 2. Series (one-dimensional labeled array):
# print(type(weather_data["temp"]))

# Convert CSV to a Dictionary.
# weather_dict = weather_data.to_dict()
# print(weather_dict)

# Convert CSV to a List.
# weather_list = weather_data["temp"].to_list()
# print(weather_list)

# Average Week Temperature.
# average_temp = round(weather_data["temp"].mean())
# print(f"Average Week Temperature is: {average_temp}")

# Maximum Week Temperature.
# max_temp = weather_data["temp"].max()
# print(f"Max Week Temperature is: {max_temp}")

# Exist Two Ways to Get Data in Columns.
# 1. Using like a dictionary by [""]
# print(weather_data["temp"])
# 2. Using like an attribute
# print(weather_data.temp)

# Get Data in Row.
# monday_data = weather_data[weather_data.day == "Monday"]
# print(monday_data)

# Get Row of Maximum Week Temperature.
# max_temp_data = weather_data[weather_data.temp == weather_data.temp.max()]
# print(max_temp_data)

# Convert Monday Temperature from Celsius to Fahrenheit.
# monday_data = weather_data[weather_data.day == 'Monday']
# monday_temp = monday_data.temp[0]
# monday_temp_fahr = monday_temp * 9/5 + 32
# print(monday_temp_fahr)

# Create Dataframe from Scratch.
# Example of Dictionary:
# student_dict = {
#     "student": ["Fabio", "Isabela", "Alex"],
#     "scores": [76, 88, 57]
# }
#
# student_data = pandas.DataFrame(student_dict)
# print(student_data)

# ----------------------------------------------------------------------------------------------------------------------