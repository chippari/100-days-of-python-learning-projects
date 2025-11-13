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

# Open Weather Map API KEY Setup.
API_KEY = "SET_YOUR_API_KEY"

MY_LAT = "SET_YOUR_LAT"
MY_LON = "SET_YOUR_LON"

OWN_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"

# > Main ---------------------------------------------------------------------------------------------------------------

def main():
    # Set Parameters accordingly from API Endpoint.
    parameters = {
        "lat": MY_LAT,
        "lon": MY_LON,
        "appid": API_KEY,
    }

    # Get API Response from API Endpoint.
    response = requests.get(url=OWN_ENDPOINT, params=parameters)

    # Raise an exception if there is an error.
    response.raise_for_status()

    # Get Data from API Response.
    data = response.json()
    print(data)


if __name__ == '__main__':
    main()

# ----------------------------------------------------------------------------------------------------------------------
