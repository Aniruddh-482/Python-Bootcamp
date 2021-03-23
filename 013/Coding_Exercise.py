# Exercise-01
# Debug Odd or Even
# Instructions
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


# Exercise-02
# Debug Leap Year
# Instructions
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


# Exercise-03
# Debug FizzBuzz
# Instructions
# Read this the code in main.py
# Spot the problems 🐞.
# Modify the code to fix the program.
# No shortcuts - don't copy-paste to replace the code entirely with a working solution.
# The code needs to print the solution to the FizzBuzz game.
# Your program should print each number from 1 to 100 in turn.
# When the number is divisible by 3 then instead of printing the number it should print "Fizz".
# When the number is divisible by 5, then instead of printing the number it should print "Buzz".
# And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz".
for number in range(1, 101):
  if number % 3 == 0 or number % 5 == 0:
    print("FizzBuzz")
  if number % 3 == 0:
    print("Fizz")
  if number % 5 == 0:
    print("Buzz")
  else:
    print([number])
# Errors-
# line_02: 'or' is used on the place of 'and', so it prints 'FizzBuzz' every time either given number is divisible by 3 or 5. 
# line_04 and line_06: 'if' statement is used on the place of 'elif' statement, so compiler checks all the coditions and prints all the statements for all true conditions.
# line_09: prints each numbers in bracket(as they are in a list)

# Solution : 
for number in range(1, 101):
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number)















