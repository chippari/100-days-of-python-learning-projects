# ----------------------------------------------------------------------------------------------------------------------
# > Day 25 - Squirrel Count Project ------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# > File: main.py
# > Module: Main Module
# > Description: Entry point of the application; initializes and runs the main logic.
# > Author: Fabio Chippari
# > Created: 2025-10-18
# ----------------------------------------------------------------------------------------------------------------------

import pandas
from numpy.matlib import empty

# Get Squirrel Data by Reading its CSV File.
squirrel_data = pandas.read_csv("squirrel_data_central_park.csv")

# Get each Color on Primary Fur Color and count it.
grey_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
cin_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])

# Create a Squirrels Dictionary with Fur Color and Count for each.
squirrels_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, cin_squirrels_count, black_squirrels_count]
}

# Create a Squirrels Data Frame with Squirrels Dictionary and Convert it to a new CSV File.
squirrels_df = pandas.DataFrame(squirrels_dict)
squirrels_df.to_csv("squirrels_count.csv")

# ----------------------------------------------------------------------------------------------------------------------