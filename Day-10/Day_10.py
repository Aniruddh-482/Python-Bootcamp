# Functions with Outputs

# def my_function():
# 	result = 3 * 2
# 	return result  # returns output
# output = my_function()  # Output my_function returns result(6)

# Create a program that change the first letter of first name and last name from lower case to upper case
def format_name(first_name, last_name):
    first_name = first_name.title()
    last_name = last_name.title()
    return first_name, last_name
f_name = input("What is your first name?: ")
l_name = input("What is your last name?: ")
output = format_name(f_name, l_name)
print (output)
# Output ==>
# What is your first name?: AniRuddh
# What is your last name?: uPAdhyay
# ('Aniruddh', 'Upadhyay')
# or
def format_name(f_name, l_name):
    print(f_name.title())
    print(l_name.title())
format_name("anGELa","YU")
# Output ==>
# Angela
# Yu
# or
def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
	print(f"{formated_f_name} {formated_l_name}")
format_name("anGELa","YU")
# Output ==>
# Angela Yu
# or
def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
	return f"{formated_f_name} {formated_l_name}"
formated_string = format_name("anGELa","YU")
print(formated_string)
# Output ==>
# Angela Yu
# or
def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"
print(format_name("AnGELa","YU"))
# Output ==>
# Angela Yu

# Multiple Return Values
def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"Result: {formated_f_name} {formated_l_name}"
print(format_name(input("What is your first name? "), input("What is your last name? ")))

#Storing output in a variable
formatted_name = format_name(input("Your first name: "), input("Your last name: "))
print(formatted_name)
#or printing output directly
print(format_name(input("What is your first name? "), input("What is your last name? ")))

#Already used functions with outputs.
length = len(formatted_name)

#Return as an early exit
def format_name(f_name, l_name):
  if f_name == "" or l_name == "":
    return "You didn't provide valid inputs."
  formated_f_name = f_name.title()
  formated_l_name = l_name.title()
  return f"Result: {formated_f_name} {formated_l_name}"


# Days in Month
# Instructions
# In the starting code, you'll find the solution from the Leap Year challenge. 
# First, convert this function is_leap() so that instead of printing "Leap year." or "Not leap year." 
# it should return True if it is a leap year and return False if it is not a leap year.

# You are then going to create a function called days_in_month() which will take a year and a month as inputs, e.g.
# days_in_month(year=2022, month=2)
# And it will use this information to work out the number of days in the month, then return that as the output, e.g.:
# 28
# The List month_days contains the number of days in a month from January to December for a non-leap year. A leap year has 29 days in February.
def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False
def days_in_month(year, month):
  if is_leap(year):
    month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  else:
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]   
  return month_days[month - 1] 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
# or
def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False
def days_in_month(year, month):
# 	if month > 12 or month < 1:
# 		return "Invalid Month"
	month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
	if is_leap(year) and month == 2:
		return 29
	return month_days[month - 1]
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)


# Docstrings
# Python documentation strings (or docstrings) provide a convenient way of associating documentation with Python modules, functions, classes, and methods.
# It’s specified in source code that is used, like a comment, to document a specific segment of code. 
# Unlike conventional source code comments, the docstring should describe what the function does, not how.
# Declaring Docstrings: The docstrings are declared using ”’triple single quotes”’ or “””triple double quotes””” just below the class, method or function declaration. 
# All functions should have a docstring.
# Accessing Docstrings: The docstrings can be accessed using the __doc__ method of the object or using the help function.
# for example
#Return as an early exit
def format_name(f_name, l_name):
  """Take a first and last name and format it 
  to return the title case version of the name."""  #Docstring
  if f_name == "" or l_name == "":
    return "You didn't provide valid inputs."
  formated_f_name = f_name.title()
  formated_l_name = l_name.title()
  return f"Result: {formated_f_name} {formated_l_name}"


# Calculator Part-1: Combining Dictionaries and Functions
# Calculator
# Add
def add(n1, n2):
  return n1 + n2
# Subtract
def subtract(n1, n2):
  return n1 - n2
# Multiply
def multiply(n1, n2):
  return n1 * n2
# Divide
def divide(n1, n2):
  return n1 / n2
# Dictionary
operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}
num1 = int(input("What's the first number?: "))
for symbol in operations:
  print(symbol)
operation_symbol = input("Pick an operation from the line above: ")
num2 = int(input("What's the second number?: "))
calculation_function = operations[operation_symbol]
answer = calculation_function(num1, num2)
print(f"{num1} {operation_symbol} {num2} = {answer}")

# Calculator Part-2: Print vs Return

