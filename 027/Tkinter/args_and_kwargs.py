# Advanced Python Arguments
# Arguments with Default Values.
# For Example:
# def my_function(a=1, b=2, c=3):
# 	# Do this with a
# 	# Then do this with b
# 	# Finally do this with c
# my_function()
# If we wanted to change the value of b
# my_function(b=5)
# a and c are still take the default value.

# *args: Many Positional Arguments
# Positional Variable-Length Arguments
# Unlimited Arguments or Unlimited Positional Arguments
def add(*args):
	# print(args[1])
	for n in args:
		print(n)
# For Example:
def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

print(add(7, 7, 5, 1, 5))
# Output ==> 25

# **kwargs: Many Keyword Arguments
# Keyworded Variable-Length Arguments
# Unlimited Keyword Arguments 
def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    # print(n)

calculate(2, add=3, multiply=5)
# Output ==> 25

# How to use a **kwargs dictionary safely
class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")

my_car = Car(make="Nissan", model="Skyline")
print(my_car.model)
# Output ==> Skyline
