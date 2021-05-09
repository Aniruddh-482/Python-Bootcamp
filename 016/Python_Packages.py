# Constructing Objects and Accessing their Attributes and Methods 

# Object Construction
# import turtle
# object_name = module.class()
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


from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmanderr"])
table.add_column("Type", ["Electric", "Water", "Fire"])
# table.align = "l"  # Change Alignment to left which is by default center
print(table)
