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
bmi = round(weight / height ** 2)

if bmi < 18.5:
  print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
  print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
  print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
  print(f"Your BMI is {bmi}, you are obese.")
else:
  print(f"Your BMI is {bmi}, you are clinically obese.")

#Write a program that works out whether if a given year is a leap year. A normal year has 365 days, leap years have 366, with an extra day in February. The reason why we have leap years is really fascinating, this video does it more justice:
#https://www.youtube.com/watch?v=xX96xng7sAE
year = int(input("Which year do you want to check? "))
if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
   print("Leap year.")
else:
  print("Not leap year.")  
  
  
  
  
  
  
  
  
