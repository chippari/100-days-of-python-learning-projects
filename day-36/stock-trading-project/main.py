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
from twilio.rest import Client
import requests

# > Constants / Configuration ------------------------------------------------------------------------------------------

ALPHA_ENDPOINT = "https://www.alphavantage.co/query"
ALPHA_API_KEY = ""

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = ""

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# Twilio Account Setup.
account_sid = ""
auth_token = ""
client = Client(account_sid, auth_token)

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

    stock_data = alpha_response.json()

    # Get Yesterday and the Day Before Variables.
    yesterday = str(date.today() - timedelta(days=1))
    day_before = str(date.today() - timedelta(days=2))

    # Verify if you achieve your requests per day on your free account.
    if "Information" in stock_data:
        print("You achieve your 25 requests per day.")

        # Set Values of Stock Price from Yesterday and Day Before for learning purposes.
        stock_price_yst = 401
        stock_price_dyb = 430
    else:
        # Get Stock Price from Yesterday and Day Before.
        stock_price_yst = float(stock_data["Time Series (Daily)"][yesterday]["4. close"])
        stock_price_dyb = float(stock_data["Time Series (Daily)"][day_before]["4. close"])

    # Get Stock Price Percentage Change.
    stock_percentage_change = round(((stock_price_yst - stock_price_dyb) / stock_price_yst) * 100)

    # If Stock Price increase/decreases by 5% between yesterday and the day before yesterday, get news.
    if stock_percentage_change > 5 or stock_percentage_change < -5:
        # News API Setup.
        news_parameters = {
            "q": COMPANY_NAME,
            "from": day_before,
            "sortBy": "popularity",
            "apikey": NEWS_API_KEY
        }

        news_response = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
        news_response.raise_for_status()

        news_data = news_response.json()

        # Set the first 3 news in a list.
        main_news = []
        # Get the first 3 news pieces for the COMPANY_NAME.
        for piece in range(3):
            news_headline = news_data["articles"][piece]["title"]
            news_description = news_data["articles"][piece]["description"]

            main_news.append({"Headline": news_headline, "Brief": news_description})

        send_this = (f"TSLA: {'🔺' if stock_percentage_change > 0 else '🔻'}{abs(stock_percentage_change)}%\n"
            f"{''.join(
            f'> News {i + 1}:\n'
            f'Headline: {piece["Headline"]}\n'
            f'Brief: {piece["Brief"]}\n'
            for i, piece in enumerate(main_news)
        )}")

        # Send SMS using Twilio with the message containing Stock Percentage Change and News Together.
        message = client.messages.create(
            from_="",
            body=f"TSLA: {'🔺' if stock_percentage_change > 0 else '🔻'}{abs(stock_percentage_change)}%\n",
            to=""
        )

        print(message.status)

if __name__ == '__main__':
    main()

# ----------------------------------------------------------------------------------------------------------------------
