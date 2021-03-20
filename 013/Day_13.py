############DEBUGGING#####################

# Describe Problem
def my_function():
  for i in range(1, 20):  # Error
    if i == 20:  # i is never equal to 20 because range(n, m) function gives number from range n to m-1
      print("You got it")  # Prints nothing
my_function()

# Solution :
def my_function():
  for i in range(1, 21):
    if i == 20:
      print("You got it")  # Prints You got it
my_function()


# Reproduce the Bug
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(1, 6)  # Error
# random int gives a random number between given ends includeing those ends
print(dice_imgs[dice_num])  # prints Error sometimes when randint prints 6

# Reproduce the Bug
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = 6  # Error
print(dice_imgs[dice_num])  # prints Error everytimes

# Solution :
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5)
print(dice_imgs[dice_num])  # prints random dice image 


# Play Computer
year = int(input("What's your year of birth?"))
if year > 1980 and year < 1994:
  print("You are a millenial.")
elif year > 1994:
  # Error is there is no condition for year = 1994
  print("You are a Gen Z.")  # Prints nothing when year is 1994.

# Solution :
year = int(input("What's your year of birth?"))
if year > 1980 and year < 1994:
  print("You are a millenial.")
elif year >= 1994:
  print("You are a Gen Z.")  # Prints when year is >= 1994 You are a Gen Z.



