#  Turtle Challenge - 01: Draw a Square

# #####Turtle Intro######

# import turtle as t

# timmy_the_turtle = t.Turtle()
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("red")
# timmy_the_turtle.forward(100)
# timmy_the_turtle.backward(200)
# timmy_the_turtle.right(90)
# timmy_the_turtle.left(180)
# timmy_the_turtle.setheading(0)

# ######## Challenge 1 - Draw a Square ############

# timmy_the_turtle.left(90)
# timmy_the_turtle.forward(200)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(200)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(200)

# OR
######## Challenge 1 - Draw a Square ############
import turtle as t

timmy_the_turtle = t.Turtle()

for _ in range(4):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.left(90)

screen = t.Screen()
screen.exitonclick()

