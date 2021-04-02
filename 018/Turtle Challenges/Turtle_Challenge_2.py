#  Turtle Challenge - 02: Draw a Dashed Line

import turtle as t

tim = t.Turtle()

########## Challenge 2 - Draw a Dashed Line ##########
for _ in range(5):
    tim.forward(10)
    tim.penup()  # You can move the turtle without the turtle drawing
    tim.forward(10)
    tim.pendown()  # To tell it to draw again

screen = t.Screen()
screen.exitonclick()

# Solution:

import turtle as t

tim = t.Turtle()

########## Challenge 2 - Draw a Dashed Line ##########
for _ in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()

