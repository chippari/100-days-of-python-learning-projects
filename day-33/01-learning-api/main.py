# ----------------------------------------------------------------------------------------------------------------------
# > Day 33 - Learning about API ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# > File: main.py
# > Module: Main Module
# > Description: Entry point of the application; initializes and runs the main logic.
# > Author: Fabio Chippari
# > Created: 2025-10-26
# ----------------------------------------------------------------------------------------------------------------------
# > Imports ------------------------------------------------------------------------------------------------------------

import requests

# > Main ---------------------------------------------------------------------------------------------------------------

def main():
    # Get Response by API Endpoint.
    response = requests.get(url="http://api.open-notify.org/iss-now.json")

    # Raise an exception when there is an error on API Request.
    response.raise_for_status()

    # Get Data from API Response.
    data = response.json()
    print(data)

if __name__ == '__main__':
    main()

# ----------------------------------------------------------------------------------------------------------------------
