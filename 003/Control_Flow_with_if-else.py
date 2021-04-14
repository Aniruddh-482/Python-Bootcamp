#Write a program to check the hight of customers for rollercoaster ride
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
  print("You can ride the rollercoaster!")
else:
  print("Sorry, you have to grow taller before you can ride.")

  
# Comparision Operators

# > Greater than
# < Less than
# >= Greater than or equal to
# <= Less than or equal to
# == Equal to  #it compares the value of left side and right side
# != Not equal to

# = Equal to is a Assignment Operator that assign the value of right side to left side

# % Modulo Operation prints reminder 
# for example: 
# print(7 % 2) prints 1


# Nested if/else: 
# if-else within if-else
# Syntax
# if condition_1:
# if condition_1
#  do A
# else:
#  do B
# else:
# do this

# For Example: 
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age <= 18:
    print("Please pay $7.")
  else:
    print("Please pay $12.")
else:
  print("Sorry, you have to grow taller before you can ride.")

  
# elif statement
# if/elif/else
# Syntax
# if condition_1:
# do A
# elif condition_2:
# do B
# else:
# do this

# For Example: 
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age <= 12:
    print("Please pay $5.")
  elif age <= 18:
    print("Please pay $7.")
  else:
    print("Please pay $12.")
else:
  print("Sorry, you have to grow taller before you can ride.")

  
# Multiple if statement
# Syntax
# if condition_1:
# do A
# if condition_2:
# do B
# if condition_3:
# do C
# if all condition are true then it perform all tasks (A, B, C)

# For Example: 
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age <= 12:
    bill = 5
    print("Child ticket are $5.")
  elif age <= 18:
    bill = 7
    print("Youth ticket are $7.")
  else:
    bill = 12
    print("Adult ticket are $12.")
  wants_photo = input("Do you want a photo taken? Y or N. ")
  if wants_photo == "Y":
    bill += 3
    # Add $3 to their bill
    # print(f"Your final bill is ${bill}")
    # or
  print(f"Your final bill is ${bill}")
else:
  print("Sorry, you have to grow taller before you can ride.") 

  
# Logical Operators

# AND Operator
# A and B
# if atleast one condition is false then print False
# if both conditions are true then print true

# OR Operator
# C or D
# if atleast one condition is true then print True
# if both conditions are false then print False

# NOT Operator
# not E
# prints opposite of condition or reverse the condition
# if condition is true then print False
# if condition is False then print True

# For Example: 
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age < 12:
    bill = 5
    print("Child tickets are $5.")
  elif age <= 18:
    bill = 7
    print("Youth tickets are $7.")
  elif age >= 45 and age <= 55:
    print("Everything is going to be ok. Have a free ride on us!")
  else:
    bill = 12
    print("Adult tickets are $12.")
  
  wants_photo = input("Do you want a photo taken? Y or N. ")
  if wants_photo == "Y":
    bill += 3
  
  print(f"Your final bill is ${bill}")

else:
  print("Sorry, you have to grow taller before you can ride.")
