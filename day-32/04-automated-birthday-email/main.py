# ----------------------------------------------------------------------------------------------------------------------
# > Day 32 - Automated Birthday Wisher Email Project -------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# > File: main.py
# > Module: Main Module
# > Description: Entry point of the application; initializes and runs the main logic.
# > Author: Fabio Chippari
# > Created: 2025-10-24
# ----------------------------------------------------------------------------------------------------------------------
# > Imports ------------------------------------------------------------------------------------------------------------

import smtplib
import random
import pandas
import datetime as dt

# > Constants / Configuration ------------------------------------------------------------------------------------------

MY_EMAIL = "my@email.com"
MY_PASSWORD = "12345"

# > Main ---------------------------------------------------------------------------------------------------------------

def main():
    # Get Birthdays Data.
    birthdays_data = pandas.read_csv("birthdays.csv")
    birthdays = birthdays_data.to_dict(orient='records')

    # Get Current Datetime.
    now = dt.datetime.now()
    # Get Current Month.
    month = now.month
    # Get Current Day.
    day = now.day

    # Create a Current Birthday List.
    current_birthdays = []
    # Loop through birthdays to get the Current Birthday.
    for birthday in birthdays:
        if birthday["month"] == month:
            if birthday["day"] == day:
                current_birthdays.append(birthday)

    # Loop trough Current Birthdays to get each Birthday Data, if there is more one birthday on the same day.
    for birthday in current_birthdays:
        # Get Birthday Name and Email.
        birthday_name = birthday["name"]
        birthday_email = birthday["email"]

        # Get Random Birthday Letter from letter_templates.
        letter_file = random.choice(["letter_1.txt", "letter_2.txt", "letter_3.txt"])
        # Read Letter to Get the content.
        with open(file=f"letter_templates/{letter_file}", mode="r") as file:
            letter_content = file.read()
        # Replace [NAME] with the Birthday Name.
        letter_customized = letter_content.replace("[NAME]", birthday_name)

        # Send the Birthday Letter Customized to the Person via Email.
        with smtplib.SMTP("smtp.gmail.com") as connection:
            # Secure the Connection by using starttls that will encrypt your email content if anyone try to intercept.
            connection.starttls()
            # Login in to your email.
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            # Send your email to the Birthday Person.
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=birthday_email, msg=f"Subject: Happy Birthday {birthday_name}\n\n{letter_customized}")

if __name__ == '__main__':
    main()

# ----------------------------------------------------------------------------------------------------------------------
