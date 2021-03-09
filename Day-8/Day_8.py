# Function Parameters
# Functions with Inputs
# def my_function(something):  # Something = 123
	# Do this with something   #    |         |
	# Then do this             # Parameter   Argument
	# Finally do this
# my_function(123)  #or any data you want to pass to my_function
# Argument is actual piece of data thts going to be passed over to the function when its being called
# Parameter is the name of that data and we use the parameter inside the function to refer to it and do things with it

# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.
# Simple Function
def greet():
    print("Hello")
    print("How do you do?")
    print("Isn't the weather nice today?")
greet()
# With Inputs or With Parameters
# Function that allows for input
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")
    print("Isn't the weather nice today?")
greet_with_name("Ansh")

#Functions with more than 1 input
def greet_with(name, location):
  print(f"Hello {name}")
  print(f"What is it like in {location}?")
#Calling greet_with() with Positional Arguments
greet_with("Jack Bauer", "Nowhere")
#vs.
greet_with("Nowhere", "Jack Bauer")
#Calling greet_with() with Keyword Arguments
greet_with(location="London", name="Angela")
# 
greet_with("Ansh", "Ujjain")  # Positional Argument
greet_with(location = "Ujjain", name = "Ansh")  # Keyword Argument


# Area Calculation Exercise
# You are painting a wall. The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall. 
# Given a random height and width of wall, calculate how many cans of paint you'll need to buy.
# number of cans = (wall height ✖️ wall width) ÷ coverage per can.
# e.g. Height = 2, Width = 4, Coverage = 5
# number of cans = (2 ✖️ 4) ÷ 5
#                      = 1.6
#                      = 1.6
# But because you can't buy 0.6 of a can of paint, the result should be rounded up to 2 cans.
import math
def paint_calc(height, width, cover):
    number_of_cans = math.ceil(height * width / cover)
    print(f"You'll need {number_of_cans} cans of paint.")
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
# or
import math
def paint_calc(height, width, cover):
	area = height * width
	num_of_cans = math.ceil(area / cover)
    print(f"You'll need {num_of_cans} cans of paint.")
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)


# Prime Number Checker
# Prime Numbers
# Instructions
# Prime numbers are numbers that can only be cleanly divided by itself and 1.
# https://en.wikipedia.org/wiki/Prime_number
# You need to write a function that checks whether if the number passed into it is a prime number or not.
def prime_checker(number):
    flag = 0
    for num in range(2, number):
        if number % num == 0:
            flag = 1
    if flag == 0:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")
n = int(input("Check this number: "))
prime_checker(number=n)
# or
def prime_checker(number):
	is_prime = True
	for i in range(2, number):
		if number % i == 0:
			is_prime = False
	if is_prime:
		print("It's a prime number.")
    else:
        print("It's not a prime number.")
n = int(input("Check this number: "))
prime_checker(number=n)

