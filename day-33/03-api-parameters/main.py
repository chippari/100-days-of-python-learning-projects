# ----------------------------------------------------------------------------------------------------------------------
# > Day 33 - Learning about API Parameters -----------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# > File: main.py
# > Module: Main Module
# > Description: Entry point of the application; initializes and runs the main logic.
# > Author: Fabio Chippari
# > Created: 2025-10-26
# ----------------------------------------------------------------------------------------------------------------------
# > Imports ------------------------------------------------------------------------------------------------------------

import requests

# > Constants / Configuration ------------------------------------------------------------------------------------------

MY_LAT = -23.550520
MY_LONG = -46.633308

# > Main ---------------------------------------------------------------------------------------------------------------

def main():
    # Set Parameters accordingly from API Endpoint.
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    # Get API Response from API Endpoint.
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    # Raise an exception if there is an error.
    response.raise_for_status()

    # Get Data from API Response.
    data = response.json()

    # Get Sunrise & Sunset from data.
    sunrise_hour = data["results"]["sunrise"].split("T")[1].split(":")[0]
    sunset_hour = data["results"]["sunset"].split("T")[1].split(":")[0]

    print(f"Sunrise Hour: {sunrise_hour}")
    print(f"Sunset Hour: {sunset_hour}")


if __name__ == '__main__':
    main()

# ----------------------------------------------------------------------------------------------------------------------
