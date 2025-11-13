# ----------------------------------------------------------------------------------------------------------------------
# > Day 35 - Learning about API Key ------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# > File: main.py
# > Module: Main Module
# > Description: Entry point of the application; initializes and runs the main logic.
# > Author: Fabio Chippari
# > Created: 2025-11-12
# ----------------------------------------------------------------------------------------------------------------------
# > Imports ------------------------------------------------------------------------------------------------------------

import requests

# > Constants / Configuration ------------------------------------------------------------------------------------------

# To get API KEY go to https://openweathermap.org/
API_KEY = ""

OWN_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
MY_LAT = -21.4587581
MY_LON = -54.3698517

# > Main ---------------------------------------------------------------------------------------------------------------

def main():
    # Set Parameters accordingly from API Endpoint.
    weather_parameters = {
        "lat": MY_LAT,
        "lon": MY_LON,
        "appid": API_KEY,
        "cnt": 4
    }

    # Get API Response from API Endpoint.
    response = requests.get(url=OWN_ENDPOINT, params=weather_parameters)

    # Raise an exception if there is an error.
    response.raise_for_status()

    # Get Data from API Response.
    weather_data = response.json()

    for time in weather_data["list"]:
        # Get Weather Condition Codes.
        weather_code = time["weather"][0]["id"]
        # Get Weather Condition.
        weather_condition = time["weather"][0]["main"]
        # Get Weather Hour.
        weather_hour = time["dt_txt"].split(" ")[1].split(":")[0]

        if weather_code < 700:
            print(f"Bring your umbrella! The weather condition is {weather_condition} at {weather_hour} hours.")
        else:
            print(f"You don't have to worry at {weather_hour} hours, because the weather condition is {weather_condition}!")


if __name__ == '__main__':
    main()

# ----------------------------------------------------------------------------------------------------------------------
