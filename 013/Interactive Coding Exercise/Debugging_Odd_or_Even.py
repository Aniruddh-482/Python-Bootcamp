# Exercise-01: 

# Debug Odd or Even #
# ----------------- #

# Instructions:
# Read this the code in main.py
# Spot the problems 🐞.
# Modify the code to fix the program.
# Fix the code so that it works and passes the tests when you submit.

number = int(input("Which number do you want to check?"))
if number % 2 = 0:  # Syntax Error
# '=' is used on the place of '=='
  print("This is an even number.")
else:
  print("This is an odd number.")

# Solution : 
number = int(input("Which number do you want to check?"))
if number % 2 == 0:
  print("This is an even number.")
else:
  print("This is an odd number.")
  
  
