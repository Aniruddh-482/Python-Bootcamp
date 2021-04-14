# Write a program that works out whether if a given year is a leap year.
# A normal year has 365 days, leap years have 366, with an extra day in February. 
# The reason why we have leap years is really fascinating, this video does it more justice:
# https://www.youtube.com/watch?v=xX96xng7sAE

year = int(input("Which year do you want to check? "))

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
   print("Leap year.")
else:
  print("Not leap year.")  
  
