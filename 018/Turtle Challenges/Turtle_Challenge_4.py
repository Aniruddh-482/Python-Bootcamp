#  Turtle Challenge - 04: Generate a Random Walk

# What is Random Walk: https://en.wikipedia.org/wiki/Random_walk

import turtle as t
import random

tim = t.Turtle()

########## Challenge 4 - Random Walk ##########
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def move():
    random_direction = random.randint(1, 4)
    if random_direction == 1:
        tim.left(90)
    elif random_direction == 2:
        tim.right(90)
    # elif random_direction == 3:  # For more directions
    #     tim.left(180)
    # elif random_direction == 4:
        tim.right(180)
    tim.forward(20)

def change_color():
    R = random.random()
    B = random.random()
    G = random.random()

    tim.color(R, G, B)

tim.speed(10)
tim.width(width=6)
count = 0
while count < 500:  # How many times you want random walk
    change_color()
    move()
    count += 1

screen = t.Screen()
screen.exitonclick()

# Solution:

import turtle as t
import random

tim = t.Turtle()

########### Challenge 4 - Random Walk ########
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")

for _ in range(200):
    tim.color(random.choice(colours))
    tim.forward(30)
    tim.setheading(random.choice(directions))
