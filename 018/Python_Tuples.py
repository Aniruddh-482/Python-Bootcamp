# Python Tuples
# Example:
my_tuple = (1, 3, 8)
print(my_tuple[2])
# Prints 8
# We can't change the value of tuple.
# Example:
# my_tuple[2] = 12
# gives error

# To generate a random color 
# RGB Calculator: https://www.w3schools.com/colors/colors_rgb.asp

import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

########### Challenge 4 - Random Walk ########
# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def random_color():
    R = random.randint(0, 255)
    G = random.randint(0, 255)
    B = random.randint(0, 255)

    tim.color(R, G, B)

directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")

for _ in range(200):
    random_color()
    tim.forward(30)
    tim.setheading(random.choice(directions))

# OR
import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

########### Challenge 4 - Random Walk ########
# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def random_color():
    R = random.randint(0, 255)
    G = random.randint(0, 255)
    B = random.randint(0, 255)

    # tim.color(R, G, B)
    random_color = (R, G, B)
    return random_color

directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")

for _ in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))
