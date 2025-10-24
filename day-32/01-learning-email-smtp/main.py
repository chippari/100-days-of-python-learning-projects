# ----------------------------------------------------------------------------------------------------------------------
# > Day 32 - Learning about Email SMTP ---------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# > File: main.py
# > Module: Main Module
# > Description: Entry point of the application; initializes and runs the main logic.
# > Author: Fabio Chippari
# > Created: 2025-10-24
# ----------------------------------------------------------------------------------------------------------------------
# > Imports ------------------------------------------------------------------------------------------------------------

import smtplib

# > Main ---------------------------------------------------------------------------------------------------------------

def main():
    # Get Your Email and Password.
    my_email = "example@gmail.com"
    my_password = "123456"

    # Create a Connection using smtplib and put your SMTP Provider.
    with smtplib.SMTP('smtp.gmail.com') as connection:
        # Secure the Connection by using starttls that will encrypt your email content if anyone try to intercept.
        connection.starttls()
        # Login in to your email.
        connection.login(user=my_email, password=my_password)
        # Send your email to someone.
        connection.sendmail(from_addr=my_email, to_addrs="someone@gmail.com",
                            msg="Subject:Hello\n\nThis where you put your message!")

if __name__ == '__main__':
    main()

# ----------------------------------------------------------------------------------------------------------------------
