# ----------------------------------------------------------------------------------------------------------------------
# > Day 34 - GUI Quiz App Project --------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# > File: data.py
# > Module: Data Module
# > Description:
# > Author: Fabio Chippari
# > Created: 2025-10-27
# ----------------------------------------------------------------------------------------------------------------------
# > Imports ------------------------------------------------------------------------------------------------------------

import requests

# > Data ---------------------------------------------------------------------------------------------------------------

# Set Parameters from Trivia API
parameters = {
    "amount": 10,
    "type": "boolean"
}

# Get Response from Trivia Endpoint API.
response = requests.get(url="https://opentdb.com/api.php", params=parameters)
# Raise an exception if there is an error.
response.raise_for_status()

# Get Data from API Response.
data = response.json()
# Get Question Data from Data Results.
question_data = data["results"]

# ----------------------------------------------------------------------------------------------------------------------
