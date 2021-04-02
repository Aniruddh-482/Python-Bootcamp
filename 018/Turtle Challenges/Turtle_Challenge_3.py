#  Turtle Challenge - 03: Drawing Different Shapes

import turtle as t

tim = t.Turtle()

########## Challenge 3 - Draw Shapes ##########
import random as r

def change_color():  # To Change color
    R = r.random()
    B = r.random()
    G = r.random()

    tim.color(R, G, B)

# For Triangle
change_color()
for _ in range(3):
    tim.right(120)
    tim.forward(100)
# For Square
change_color()
for _ in range(4):
    tim.right(90)
    tim.forward(100)
# For Pentagon
change_color()
for _ in range(5):
    tim.right(72)
    tim.forward(100)
# For Hexagon
change_color()
for _ in range(6):
    tim.right(60)
    tim.forward(100)
# For Heptagon
change_color()
for _ in range(7):
    tim.right(51.4)
    tim.forward(100)
# For Octagon
change_color()
for _ in range(8):
    tim.right(45)
    tim.forward(100)
# For Nonagon
change_color()
for _ in range(9):
    tim.right(40)
    tim.forward(100)
# For Decagon
change_color()
for _ in range(10):
    tim.right(36)
    tim.forward(100)

screen = t.Screen()
screen.exitonclick()

# Solution:

import turtle as t
import random

tim = t.Turtle()

########### Challenge 3 - Draw Shapes ########

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

for shape_side_n in range(3, 10):
    tim.color(random.choice(colours))
    draw_shape(shape_side_n)

    
