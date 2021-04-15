# Working with the datetime Module #
# -------------------------------- #

import datetime as dt

now = dt.datetime.now()

year = now.year   
print(year)            # Prins current year

month = now.month
print(month)           # Prins current month

day_of_week = now.weekday()
print(day_of_week)     # Prints current day of week

date_of_birth = dt.datetime(year=1995, month=12, day=15, hour=4)
print(date_of_birth)   # Prints defaulte value (1995-12-15 04:00:00)

