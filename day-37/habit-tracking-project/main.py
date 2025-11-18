# ----------------------------------------------------------------------------------------------------------------------
# > Day 37 - Learning about API Key ------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# > File: main.py
# > Module: Main Module
# > Description: Entry point of the application; initializes and runs the main logic.
# > Author: Fabio Chippari
# > Created: 2025-11-17
# ----------------------------------------------------------------------------------------------------------------------
# > Imports ------------------------------------------------------------------------------------------------------------

import requests

# > Constants / Configuration ------------------------------------------------------------------------------------------

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USERNAME = ""
PIXELA_TOKEN = ""

# > Main ---------------------------------------------------------------------------------------------------------------

def main():
    # Create User using Pixela API.
    # pixela_user_params = {
    #     "token": "",
    #     "username": "",
    #     "agreeTermsOfService": "yes",
    #     "notMinor": "yes",
    # }
    #
    # pixela_user_response = requests.post(url=PIXELA_ENDPOINT, json=pixela_user_params)
    # print(pixela_user_response.text)

    # Create New Pixelation Graph using Pixela API.
    graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

    graph_headers = {
        "X-USER-TOKEN": PIXELA_TOKEN
    }

    graph_config = {
        "id": "",
        "name": "",
        "unit": "",
        "type": "",
        "color": "",
        "timezone": "",
    }

    graph_response = requests.post(url=graph_endpoint, headers=graph_headers, json=graph_config)
    print(graph_response.text)

if __name__ == '__main__':
    main()

# ----------------------------------------------------------------------------------------------------------------------
