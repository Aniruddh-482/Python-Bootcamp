###################### DEBUGGING #####################

# 1.Describe Problem
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


# 2.Reproduce the Bug
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


# 3.Play Computer
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


# 4.Fix the Errors
age = (input("How old are you?")  # string
if age > 18:
print("You can drive at age {age}.")  # Errors
# Error-01 : Indentation error
# Error-02 : Logical Error 

# So;ution : 
age = int(input("How old are you?"))  
if age > 18 :
  print(f"You can drive at age {age}.")  # Prints "You can drive at age {given age}."


# 5.Print is Your Friend
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
# print(pages)  # Prints given input
word_per_page == int(input("Number of words per page: ")) # Error
# '==' is used on in the place of '='
# print(word_per_page)  # Prints 0 on any input
total_words = pages * word_per_page  # Given input * 0 = 0
print(total_words)  # Prints 0

# Solution : 
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
# print(pages)  # Prints given input(pages)
word_per_page = int(input("Number of words per page: "))
# print(word_per_page)  # Prints given input(word_per_page)
total_words = pages * word_per_page
print(total_words)  # Prints output


# 6.Use a Debugger
# http://www.pythontutor.com/visualize.html#mode=edit
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
  b_list.append(new_item)  # Error : Indentation Error
  print(b_list)
mutate([1,2,3,5,8,13])  # Prints wrong output(26)

# Solution :
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
    b_list.append(new_item)
  print(b_list)
mutate([1,2,3,5,8,13])  # Prints [2, 4, 6, 10, 16, 26]


# 7.Take abrek and  think again
# 8.Ask a friend for help 
# 9.Run often 
# Run the program after every editing
# 10.Search Stack Overflow for Errors
# https://stackoverflow.com/

