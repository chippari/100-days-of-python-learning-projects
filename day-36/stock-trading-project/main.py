# ----------------------------------------------------------------------------------------------------------------------
# > Day 35 - Stock Trading News Alert Project --------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# > File: main.py
# > Module: Main Module
# > Description: Entry point of the application; initializes and runs the main logic.
# > Author: Fabio Chippari
# > Created: 2025-11-13
# ----------------------------------------------------------------------------------------------------------------------
# > Instructions -------------------------------------------------------------------------------------------------------

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

## STEP 3: Use https://www.twilio.com
# Send a separate message with the percentage change and each article's title and description to your phone number.

# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to
file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height
of the coronavirus market crash.
or
TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to
file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height
of the coronavirus market crash.
"""

# > Imports ------------------------------------------------------------------------------------------------------------

from datetime import date, timedelta
import requests

# > Constants / Configuration ------------------------------------------------------------------------------------------

ALPHA_ENDPOINT = "https://www.alphavantage.co/query"
ALPHA_API_KEY = ""

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# > Main ---------------------------------------------------------------------------------------------------------------

def main():
    # Alpha Vantage API Setup.
    alpha_parameters = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK,
        "apikey": ALPHA_API_KEY
    }

    alpha_response = requests.get(url=ALPHA_ENDPOINT, params=alpha_parameters)
    alpha_response.raise_for_status()

    data = alpha_response.json()
    # print(data["Time Series (Daily)"])

    # Set in a variable Yesterday and the Day Before.
    today = date.today()
    yesterday = today - timedelta(days=1)
    day_before_yesterday = yesterday - timedelta(days=1)

    print(today, yesterday, day_before_yesterday)


    pass

if __name__ == '__main__':
    main()

# ----------------------------------------------------------------------------------------------------------------------
