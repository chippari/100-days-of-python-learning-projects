# ----------------------------------------------------------------------------------------------------------------------
# > Day 32 - Automated Motivational Quote Email Project ----------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# > File: main.py
# > Module: Main Module
# > Description: Entry point of the application; initializes and runs the main logic.
# > Author: Fabio Chippari
# > Created: 2025-10-24
# ----------------------------------------------------------------------------------------------------------------------
# > Imports ------------------------------------------------------------------------------------------------------------

import pandas
import random
import smtplib
import datetime as dt

# > Constants / Configuration ------------------------------------------------------------------------------------------

MY_EMAIL = "example@gmail.com"
MY_PASSWORD = "12345"

# > Main ---------------------------------------------------------------------------------------------------------------

def main():
    # TODO: Send a motivational quote via email on the current weekday.
    # Get Current Datetime.
    now = dt.datetime.now()
    # Get Current Weekday.
    weekday = now.weekday()
    weekday_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    # Get Quote Data and Set to be like a list.
    quote_data = pandas.read_csv("quotes.txt")
    quote_list = quote_data.values
    # Get Random Quote of the Day from the list.
    quote = random.choice(quote_list)[0]

    # If it's Friday send a motivational quote email.
    if "Friday" == weekday_list[weekday]:
        # Create a Connection using smtplib and put your SMTP Provider.
        with smtplib.SMTP("smtp.gmail.com") as connection:
            # Secure the Connection by using starttls that will encrypt your email content if anyone try to intercept.
            connection.starttls()
            # Login in to your email.
            connection.login(MY_EMAIL, MY_PASSWORD)
            # Send your email to someone.
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=f"Subject: Motivational Quote\n\n{quote}")

if __name__ == '__main__':
    main()

# ----------------------------------------------------------------------------------------------------------------------
