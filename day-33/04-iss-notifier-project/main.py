# ----------------------------------------------------------------------------------------------------------------------
# > Day 33 - ISS Overhead Notifier Project -----------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# > File: main.py
# > Module: Main Module
# > Description: Entry point of the application; initializes and runs the main logic.
# > Author: Fabio Chippari
# > Created: 2025-10-26
# ----------------------------------------------------------------------------------------------------------------------
# > Imports ------------------------------------------------------------------------------------------------------------

import requests
import smtplib
import time
from datetime import datetime

# > Constants / Configuration ------------------------------------------------------------------------------------------

MY_LAT = -23.550520
MY_LONG = -46.633308
MY_EMAIL = "my@email.com"
MY_PASSWORD = "12345"

# > Functions ----------------------------------------------------------------------------------------------------------
# >> Sunrise & Sunset Times --------------------------------------------------------------------------------------------
def is_night():
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
    sunrise_hour = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset_hour = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    # Get Currently Hour from Now.
    currently_hour = datetime.now().hour

    if currently_hour >= sunset_hour or currently_hour <= sunrise_hour:
        return True
    else:
        return False

# >> Iss Position ------------------------------------------------------------------------------------------------------
def is_iss_overhead():
    # Get Response by API Endpoint.
    response = requests.get(url="http://api.open-notify.org/iss-now.json")

    # Raise an exception when there is an error on API Request.
    response.raise_for_status()

    # Get Data from API Response.
    data = response.json()
    # Get Latitude & Longitude from ISS Position.
    iss_lat = float(data["iss_position"]["latitude"])
    iss_lng = float(data["iss_position"]["longitude"])

    # If My Latitude & Longitude is within +5 or -5 degrees of the ISS Position, return TRUE.
    if MY_LAT - 5 <= iss_lat <= MY_LAT + 5 and MY_LONG - 5 <= iss_lng <= MY_LONG + 5:
        return True
    else:
        return False

# > Main ---------------------------------------------------------------------------------------------------------------

def main():
    while True:
        # Run code every 60 seconds.
        time.sleep(60)

        # If ISS is close to My Current Position, and it's currently dark. Then email me to look up.
        if is_iss_overhead() and is_night():
            with smtplib.SMTP('smtp.gmail.com') as connection:
                # Secure the Connection by using starttls that will encrypt your email content if anyone try to intercept.
                connection.starttls()
                # Login in to your email.
                connection.login(user=MY_EMAIL, password=MY_PASSWORD)
                # Email me.
                connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg="Subject: LOOK UP NOW\n\nThe ISS is above you in the sky!")
        elif is_iss_overhead():
            print("The ISS is above you in the sky, but you cannot see because is day.")
        else:
            print("Sorry, the ISS is not above you in the sky at this moment.")

if __name__ == '__main__':
    main()

# ----------------------------------------------------------------------------------------------------------------------
