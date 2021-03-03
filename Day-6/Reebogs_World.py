# # Defining Functions
# def function_name():
#   # do this
#   # than do this
#   # finally do this
# # Calling Functions
# function_name()
# # for using the we had to call it

# Reeborg's World
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=worlds%2Ftutorial_en%2Falone.json
move()
turn_left()
# defining a funtion to turn around
def turn_around():
  turn_left()
  turn_left()
turn_around()
# define a function to turn right
def turn_right():
  turn_left()
  turn_left()
  turn_left()
turn_right()
# or
def turn_right():
  turn_around()
  turn_left()
turn_right()
# by using turn_right() function create a new function which makes a square
# Draw Square
def square():
  move()
  turn_right()
  turn_right()
  turn_right()
  move()
  turn_right()
  turn_right()
  turn_right()
  move()
  turn_right()
  turn_right()
  turn_right()
  move()
square()
or
turn_left()
move()
turn_right()
move()
turn_right()
move()
turn_right()
move()

# The Hurdles Loop Challenge
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json
# Hurdles race
# Reeborg has entered a hurdles race. Make him run the course, following the path shown.
# What you need to know
# The functions move() and turn_left().
move()
turn_left()
move()
turn_right()
move()
turn_right()
move()
turn_left()
#1st Jump
move()
turn_left()
move()
turn_right()
move()
turn_right()
move()
turn_left()
#2nd Jump
move()
turn_left()
move()
turn_right()
move()
turn_right()
move()
turn_left()
#3rd Jump
move()
turn_left()
move()
turn_right()
move()
turn_right()
move()
turn_left()
#4th Jump
move()
turn_left()
move()
turn_right()
move()
turn_right()
move()
turn_left()
#5th Jump
move()
turn_left()
move()
turn_right()
move()
turn_right()
move()
# #!!You Win!!
# More advanced
# You may have noticed that your solution has some repeated patterns. 
# If you know how to define functions, define a function named jump() and use it to simplify your program.
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
jump()  #1st Jump
jump()  #2nd Jump
jump()  #3rd Jump
jump()  #4th Jump
jump()  #5th Jump
jump()  #6th Jump
# By Using For Loop
for step in range(6):  #(0, 6)
  jump()  #Jumps 6 times
# By Using While Loop
number_of_hurdles = 6
while number_of_hurdles > 0:
  jump()  # Jumps 6 times
  number_of_hurdles -= 1
# #!!You Win!!
