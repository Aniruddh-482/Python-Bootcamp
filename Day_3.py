print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
  print("You can ride the rollercoaster!")
else:
  print("Sorry, you have to grow taller before you can ride.")

#Comparision Operators
# > Greater than
# < Less than
# >= Greater than or equal to
# <= Less than or equal to
# == Equal to  #it compares the value of left side and right side
# != Not equal to

# = Equal to is a Assignment Operator that assign the value of right side to left side

# % Modulo Operation prints reminder 
#for example
#print(7 % 2) prints 1

#Write a program that works out whether if a given number is an odd or even number.
number = int(input("Which number do you want to check? "))
if number % 2 == 0:
  print("This is an even number")
else:
  print("This is an odd number")

#Nested if/else
#if-else within if-else
#Syntax
#if condition_1:
# if condition_1
#  do A
# else:
#  do B
#else:
# do this
#for example
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

#elif statement
#if/elif/else
#Syntax
#if condition_1:
# do A
#elif condition_2:
# do B
#else:
# do this
#for example
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



#Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.
#It should tell them the interpretation of their BMI based on the BMI value.
#Under 18.5 they are underweight
#Over 18.5 but below 25 they have a normal weight
#Over 25 but below 30 they are slightly overweight
#Over 30 but below 35 they are obese
#Above 35 they are clinically obese.
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
