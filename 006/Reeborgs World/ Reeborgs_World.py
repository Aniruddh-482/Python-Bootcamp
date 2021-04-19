# Reeborg's World

move()
turn_left()

# defining a funtion to turn around
def turn_around():
  turn_left()
  turn_left()
turn_around()

# define a function to turn right
def turn_right():
  turn_around()
  turn_left()
turn_right()

# by using turn_right() function create a new function which makes a square
# Draw Square
def square():
  turn_left()
  move()
  turn_right()
  move()
  turn_right()
  move()
  turn_right()
  move()

