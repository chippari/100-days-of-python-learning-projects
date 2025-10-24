# ----------------------------------------------------------------------------------------------------------------------
# > Day 32 - Learning about Datetime Module ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# > File: main.py
# > Module: Main Module
# > Description: Entry point of the application; initializes and runs the main logic.
# > Author: Fabio Chippari
# > Created: 2025-10-24
# ----------------------------------------------------------------------------------------------------------------------
# > Imports ------------------------------------------------------------------------------------------------------------

import datetime as dt

# > Main ---------------------------------------------------------------------------------------------------------------

def main():
    # Get Current Datatime.
    now = dt.datetime.now()
    # Get Current Year.
    year = now.year
    # Get Current Moth.
    month = now.month
    # Get Current Week Day.
    day_of_week = now.weekday()
    print(f"Year: {year}, Month: {month}, Day of Week: {day_of_week}")

    # Create and Get a specific Day of your choice, like your birthdate.
    date_of_birth = dt.datetime(year=2010, month=10, day=10, hour=10)
    print(f"Date of Birth: {date_of_birth}")

if __name__ == '__main__':
    main()

# ----------------------------------------------------------------------------------------------------------------------
