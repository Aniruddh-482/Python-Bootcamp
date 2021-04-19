# Defining and Calling Functions in Python

# Functions has parenthesis

# # Built-in Functions
print("Hello!")
num_char = len("Hello!")
print(num_char)
# print() is built-in function

# Defining a function
def my_function():
  print("Hello")
  print("Bye")
my_function()  # Calling of function

# # Defining Functions
# def function_name():
#   # do this
#   # than do this
#   # finally do this
# # Calling Functions
# function_name()
# # for using the function we had to call it

# Indentation
# ---------------------
# |def my_function(): | #Line 1
# |....print("Hello") | #Line 2
# |....print("World") | #Line 3
# ---------------------
# print("World")      #Line 4
# . = 'space' in above particular code
# Line 1, 2 and 3 are intended on the other hand Line 4 is not intended
# for example
# ---------------------------
# |def my_function():       |  |- Function Block
# |....if sky == 'clear':   |  |- If Block
# |........print("blue")    |  |              } Intended
# |....elif sky == "cloudy":|  |- Elif Block
# |........print("grey")    |  |
# |....print("Hello")       |
# ---------------------------
# print("World")

