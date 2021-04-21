# Exercise-02: 

# Debug Leap Year #
# --------------- #

# Instructions:
# Read this the code in main.py
# Spot the problems 🐞.
# Modify the code to fix the program.
# No shortcuts - don't copy-paste to replace the code entirely with a working solution.
# Fix the code so that it works and when you hit submit it should pass all the tests.

year = input("Which year do you want to check?")  # string
# year is  string so we can not perform any operations on it
if year % 4 == 0:  # Type Error
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")

# Solution : 
year = int(input("Which year do you want to check?"))
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
