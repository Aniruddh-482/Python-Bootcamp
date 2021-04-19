# The Hurdles Loop Challenge #
# -------------------------- #

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

# 1st Jump
move()
turn_left()
move()
turn_right()
move()
turn_right()
move()
turn_left()

# 2nd Jump
move()
turn_left()
move()
turn_right()
move()
turn_right()
move()
turn_left()

# 3rd Jump
move()
turn_left()
move()
turn_right()
move()
turn_right()
move()
turn_left()

# 4th Jump
move()
turn_left()
move()
turn_right()
move()
turn_right()
move()
turn_left()

# 5th Jump
move()
turn_left()
move()
turn_right()
move()
turn_right()
move()

# # !!You Win!! # #


# More advanced: 

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

# For Loops
# for items in list_of_items:
#   # Do something to each item
# By Using For Loop
for step in range(6):  #(0, 6)
  jump()  #Jumps 6 times

# While loops
# while something_is_true:
#   # Do something repeatedly
# By Using While Loop
number_of_hurdles = 6
while number_of_hurdles > 0:
  jump()  # Jumps 6 times
  number_of_hurdles -= 1
# # !!You Win!! # #

# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

