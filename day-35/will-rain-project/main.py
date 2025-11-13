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
from twilio.rest import Client

# > Constants / Configuration ------------------------------------------------------------------------------------------

# Open Weather Map API KEY Setup.
API_KEY = "SET_YOUR_API_KEY"

MY_LAT = "SET_YOUR_LAT"
MY_LON = "SET_YOUR_LON"

OWN_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"

# Twilio Account Setup.
account_sid = "SET_YOUR_SID"
auth_token = "SET_YOUR_AUTH_TOKEN"
client = Client(account_sid, auth_token)

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

    # Set a variable if it will rain.
    will_rain = False

    for time in weather_data["list"]:
        # Get Weather Condition Codes.
        weather_code = time["weather"][0]["id"]

        if weather_code < 700:
            will_rain = True

    if will_rain:
        message = client.messages.create(
            from_="TWILIO_NUMBER",
            body="It's going to rain today. Remember to bring an umbrella!",
            to="YOUR_NUMBER"
        )

        print(message.status)

if __name__ == '__main__':
    main()

# ----------------------------------------------------------------------------------------------------------------------
