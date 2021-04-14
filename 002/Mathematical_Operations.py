# Mathematical Operations in Python

# '+' Addition
3 + 5

# '-' Substraction
7 - 4

# '*' Multiplicaton
3 * 2

# '/' Division
6 / 3 
# it always print a floating point number
# for example print(type(6 / 3)) prints 2.0

# '**' Exponential
2 ** 2 # print(2 ** 2) prints 4


# Python follows PEMDAS

# PEMDAS:
# Parentheses ()
# Exponents **
# Multiplicaton *
# Division /
# Addition +
# Substraction -
# Order goes from left to right

# PEMDASLR:
# ()
# **
# * /
# + -

# For Example: 
print(3 * 3 + 3 / 3 - 3)  # prints 7


# Number Manipulation
# round function
print(int(8 / 3)) # prints 2
print(round(8 / 3)) # prints 3
# round function rounds (8 / 3) into a whole number and 2.6 is written as 3
print(round(8 / 3, 2)) #rund it to decimal places 
# prints 2.67
print(round(2.6666666666, 2))
# prints 2.67    

# Flow division //
print(8 // 3) # prints 2 without converting into integer
print(type(8 // 3)) # prints integer datatype
print(type(8 / 3)) # prints float datatype

# Shorthands
# a += b    # a = a + b
# a -= b    # a = a - b
# a *= b    # a = a * b
# a /= b    # a = a / b

# F-Strings in Python
# Helps to print data of different datatypes together using single print statement
# for example
score = 0
isheight = 1.78
iswinning = True
# f-String
print(f"Your score is {score}, Your height is {isheight}, you are winning is {iswinning}")

