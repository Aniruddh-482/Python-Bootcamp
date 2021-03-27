Turtle_Graphics: https://docs.python.org/3/library/turtle.html#turtle.color
Turtle_Colors: https://cs111.wellesley.edu/labs/lab01/colors

# Constructing Objects and Accessing their Attributes and Methods
# Object Construction
# import turtle
# # object_name = module.class()
# tinny = turtle.Turtle()
# or
from turtle import Turtle, Screen
# object_name = class_name()
timmy = Turtle()
#  \         \
# object    class
print(timmy)
timmy.shape("turtle")
timmy.color("chartreuse4")
timmy.forward(100)

# Object Attributes
my_screen = Screen()
print(my_screen.canvheight)
#        \         \
#       object    attribute

# Object Methods
my_screen.exitonclick()
#  \         \
# object    Method
