# Turtle Listen Method: https://docs.python.org/3/library/turtle.html#turtle.listen

from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


screen.listen()
screen.onkey(key="space", fun=move_forwards)  # Function as Inputs
# When we pass an function as input we doesn't add '()' in the end.
screen.exitonclick()

# Python Higher Order Function
# A function that can work with another function.
# In Higher Order Function it is recommended to use Keyword Arguments instead of Positional Arguments.

