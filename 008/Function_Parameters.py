# Functions with Inputs #
# --------------------- #

# Function Parameters: 
# def my_function(something):      # Something = 123
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


# Positional vs. Keyword Arguments
# Functions with more than 1 input

def greet_with(name, location):
  print(f"Hello {name}")
  print(f"What is it like in {location}?")

# Calling greet_with() with Positional Arguments
greet_with("Jack Bauer", "Nowhere")
# vs.
greet_with("Nowhere", "Jack Bauer")

# Calling greet_with() with Keyword Arguments
greet_with(location="London", name="Angela")

greet_with("Ansh", "Ujjain")  # Positional Argument
greet_with(location = "Ujjain", name = "Ansh")  # Keyword Argument

