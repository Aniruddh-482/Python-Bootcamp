# Functions with Outputs #
# ---------------------- #

# Functions with Outputs: 
# def my_function():
# 	result = 3 * 2
# 	return result  # returns output
# output = my_function()  
# Output my_function returns result (6)

# For Example: 
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

# Storing output in a variable
formatted_name = format_name(input("Your first name: "), input("Your last name: "))
print(formatted_name)
# or printing output directly
print(format_name(input("What is your first name? "), input("What is your last name? ")))

# Return as an early exit
def format_name(f_name, l_name):
  if f_name == "" or l_name == "":
    return "You didn't provide valid inputs."
  formated_f_name = f_name.title()
  formated_l_name = l_name.title()
  return f"Result: {formated_f_name} {formated_l_name}"


# Docstrings #
# ---------- #

# Python documentation strings (or docstrings) provide a convenient way of associating documentation with Python modules, functions, classes, and methods.
# It’s specified in source code that is used, like a comment, to document a specific segment of code. 
# Unlike conventional source code comments, the docstring should describe what the function does, not how.
# Declaring Docstrings: The docstrings are declared using ”’triple single quotes”’ or “””triple double quotes””” just below the class, method or function declaration. 
# All functions should have a docstring.
# Accessing Docstrings: The docstrings can be accessed using the __doc__ method of the object or using the help function.

# For Example: 
# Return as an early exit
def format_name(f_name, l_name):
  """Take a first and last name and format it 
  to return the title case version of the name."""  #Docstring
  if f_name == "" or l_name == "":
    return "You didn't provide valid inputs."
  formated_f_name = f_name.title()
  formated_l_name = l_name.title()
  return f"Result: {formated_f_name} {formated_l_name}"
