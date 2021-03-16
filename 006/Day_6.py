# Defining and Calling Functions in Python
# Functions has parenthesis

# # Built-in Functions
# print("Hello!")
# num_char = len("Hello!")
# print(num_char)
# # print() is built-in function

# Defining a function
def my_function():
  print("Hello")
  print("Bye")
my_function()  # Calling of function

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
  
  
# Indentation
# ---------------------
# |def my_function(): | #Line 1
# |....print("Hello") | #Line 2
# |....print("World") | #Line 3
# ---------------------
# print("World")      #Line 4
# . = 'space' in above particular code
# Line 1, 2 and 3 are intended on the other hand Line 4 is not intended
# for example
# ---------------------------
# |def my_function():       |  |- Function Block
# |....if sky == 'clear':   |  |- If Block
# |........print("blue")    |  |              } Intended
# |....elif sky == "cloudy":|  |- Elif Block
# |........print("grey")    |  |
# |....print("Hello")       |
# ---------------------------
# print("World")


# For Loops
# for items in list_of_items:
#   #Do something to each item
# for number in range(a, b):
#   print(number)
# While loops
# while something_is_true:
#   #Do something repeatedly
# for example
number_of_hurdles = 6
while number_of_hurdles > 0:
  jump()  # Jumps 6 times
  number_of_hurdles -= 1
  print(number_of_hurdles)


# Reeborg's World Hurdles 2 Challenge
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%202&url=worlds%2Ftutorial_en%2Fhurdle2.json
# Hurdles race
# Reeborg has entered a hurdle race, but he does not know in advance how long the race is. 
# Make him run the course, following a path similar to the one shown, but stopping at the only flag that will be shown after the race has started.
# What you need to know
# The functions move() and turn_left().
# The condition at_goal() and its negation.
# How to use a while loop.
# Your program should also be valid for world Hurdles 1.
while at_goal() != True:
    jump()  # Jumps untill at_goal() becomes true

# Reeborg's World Hurdles 3 Challenge
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json
# Hurdles race
# Reeborg has entered a hurdle race. Make him run the course, following the path shown.
# The position and number of hurdles changes each time this world is reloaded.
# What you need to know
# The functions move() and turn_left().
# The conditions front_is_clear() or wall_in_front(), at_goal(), and their negation.
# How to use a while loop and an if statement.
# Your program should also be valid for worlds Hurdles 1 and Hurdles 2.
def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
while at_goal() != True:
    if front_is_clear() == True:
        move()  
    elif wall_in_front() == True:
        jump()

# Reeborg's World Hurdles 4 Challenge
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json
# Hurdles race
# Reeborg has entered a hurdle race. Make him run the course, following the path shown.
# The position, the height and the number of hurdles changes each time this world is reloaded.
# What you need to know
# You should be able to write programs that are valid for worlds Around 4 and Hurdles 3, and ot combine them for this last hurdles race.
# Your program should also be valid for worlds Hurdles 1, Hurdles 2 et Hurdles 3
def wall_on_left():
    wall_on_right()
    wall_on_right()
    wall_on_right()
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def jump():
    turn_left()
    while right_is_clear() != True and at_goal() != True:
        if wall_on_left() == True:
            turn_left()
        if wall_in_front() == True:
            turn_left()
        if wall_on_right() == True:
            move()
    if at_goal() == False:
        turn_right()
        move()
        turn_right()
while at_goal() != True:
    if front_is_clear() == True:
        move()  
    elif wall_in_front() == True:
        jump()


# Reeborg's World Hurdles 4 Challenge
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
# Lost in a maze
# Reeborg was exploring a dark maze and the battery in its flashlight ran out.
# Write a program using an if/elif/else statement so Reeborg can find the exit. 
# The secret is to have Reeborg follow along the right edge of the maze, turning right if it can, 
# going straight ahead if it can’t turn right, or turning left as a last resort.
# What you need to know
# The functions move() and turn_left().
# Either the test front_is_clear() or wall_in_front(), right_is_clear() or wall_on_right(), and at_goal().
# How to use a while loop and if/elif/else statements.
# It might be useful to know how to use the negation of a test (not in Python).
def turn_right():
    turn_left()
    turn_left()
    turn_left()
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif wall_on_right():
        if front_is_clear():
            move()
        else:
            turn_left()
    else:
        turn_left()
