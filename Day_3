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

  

#Write a program that works out whether if a given year is a leap year.
# A normal year has 365 days, leap years have 366, with an extra day in February. 
#The reason why we have leap years is really fascinating, this video does it more justice:
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

  

#Multiple if statement
#Syntax
#if condition_1:
# do A
#if condition_2:
# do B
#if condition_3:
# do C
#if all condition are true then it perform all tasks (A, B, C)
#for example
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
    #Add $3 to their bill
    #print(f"Your final bill is ${bill}")
    #or
  print(f"Your final bill is ${bill}")
else:
  print("Sorry, you have to grow taller before you can ride.") 

  

#Congratulations, you've got a job at Python Pizza. 
#Your first job is to build an automatic pizza order program.
#Based on a user's order, work out their final bill.
#Small Pizza: $15
#Small Pizza: $15
#Medium Pizza: $20
#Medium Pizza: $20
#Large Pizza: $25
#Large Pizza: $25
#Pepperoni for Small Pizza: +$2
#Pepperoni for Small Pizza: +$2
#Pepperoni for Medium or Large Pizza: +$3
#Pepperoni for Medium or Large Pizza: +$3
#Extra cheese for any size pizza: + $1
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L : ")
add_pepperoni = input("Do you want pepperoni? Y or N : ")
extra_cheese = input("Do you want extra cheese? Y or N : ")
bill = 0
if size == "S":
  bill = 15
  if add_pepperoni == "Y":
    bill += 2
elif size == "M":
  bill = 20
  if add_pepperoni == "Y":
    bill += 3
elif size == "L":
  bill = 25
  if add_pepperoni == "Y":
    bill += 3
if extra_cheese =="Y":
  bill += 1
print(f"Your final bill is: ${bill}.")

#or

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L : ")
add_pepperoni = input("Do you want pepperoni? Y or N : ")
extra_cheese = input("Do you want extra cheese? Y or N : ")
bill = 0
if size == "S":
  bill += 15
elif size == "M":
  bill += 20
elif size == "L": #else:
  bill += 25
if add_pepperoni == "Y":
  if size == "S":
    bill += 2
  else:
    bill += 3
if extra_cheese =="Y":
  bill += 1
print(f"Your final bill is: ${bill}.")



#Logical Operators
#AND Operator
# A and B
# if atleast one condition is false then print False
# if both conditions are true then print true
#OR Operator
# C or D
# if atleast one condition is true then print True
# if both conditions are false then print False
#NOT Operator
# not E
# prints opposite of condition or reverse the condition
# if condition is true then print False
# if condition is False then print True
#for example
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

 
  
#The lower() function changes all the letters in a string to lower case.
#https://stackoverflow.com/questions/6797984/how-do-i-lowercase-a-string-in-python

#The count() function will give you the number of times a letter occurs in a string.
#https://stackoverflow.com/questions/1155617/count-the-number-occurrences-of-a-character-in-a-string

#You are going to write a program that tests the compatibility between two people. 
#We're going to use the super scientific method recommended by BuzzFeed.
#To work out the love score between two people:
#Take both people's names and check for the number of times the letters in the word TRUE occurs. 
#Then check for the number of times the letters in the word LOVE occurs. 
#Then combine these numbers to make a 2 digit number.
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

small_name1 = name1.lower()
small_name2 = name2.lower()

t_count_name1 = small_name1.count("t")
r_count_name1 = small_name1.count("r")
u_count_name1 = small_name1.count("u")
e_count_name1 = small_name1.count("e")

true_count_name1 = t_count_name1 + r_count_name1 + u_count_name1 + e_count_name1

l_count_name1 = small_name1.count("l")
o_count_name1 = small_name1.count("o")
v_count_name1 = small_name1.count("v")
e_count_name1 = small_name1.count("e")

love_count_name1 = l_count_name1 + o_count_name1 + v_count_name1 + e_count_name1

t_count_name2 = small_name2.count("t")
r_count_name2 = small_name2.count("r")
u_count_name2 = small_name2.count("u")
e_count_name2 = small_name2.count("e")

true_count_name2 = t_count_name2 + r_count_name2 + u_count_name2 + e_count_name2

l_count_name2 = small_name2.count("l")
o_count_name2 = small_name2.count("o")
v_count_name2 = small_name2.count("v")
e_count_name2 = small_name2.count("e")

love_count_name2 = l_count_name2 + o_count_name2 + v_count_name2 + e_count_name2

total_true_count = true_count_name1 + true_count_name2
total_love_count = love_count_name1 + love_count_name2

total_score = str(total_true_count) + str(total_love_count)
score_as_int = int(total_score)

if score_as_int < 10 or score_as_int > 90:
  print(f"Your score is {score_as_int}, you go together like coke and mentos.")
elif score_as_int > 40 and score_as_int < 50:
  print(f"Your score is {score_as_int}, you are alright together.")
else:
  print(f"Your score is {score_as_int}.")  
 
  
  
#Write a program for a treasure game 
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

option_1 = input('You are at a cross road. where do you want to go? type "left" or "right" ')

if option_1 == "left":
  option_2 = input('You come to a lake. There is an island in the middle of the lake. type "wait" to wait for a boat or type "swim" to swim across. ')
  if option_2 == "wait":
    option_3 = input('You arive at the island unharmed.There is a house with Three doors. One red, one yellow, and one blue. Which colour do you choose? ')
    if option_3 == "yellow":
      print("!!!!!!!Congatulations you found the HIDDEN Treasure!!!!!!!")
      print("YOU WIN!")
      print("GAME OVER!")
    elif option_3 == "red":
      print("YOU BURNED BY FIRE")
      print("GAME OVER!")
      print("!!!BETTER LUCK NEXT TIME!!!")
    elif option_3 == "blue":
      print("YOU ENTERED IN THE ROOM OF BEASTS")
      print("GAME OVER!")
      print("!!!BETTER LUCK NEXT TIME!!!")
    else:
      print("!!!GAME OVER!!!")
  else:
    print("YOU ATTACKED BY A GROUP OF SHARKS IN THE LAKE")
    print("GAME OVER!")
    print("!!!BETTER LUCK NEXT TIME!!!")
else:
  print("YOU HAD AN ACCIDENT AND DIED!!")
  print("GAME OVER!")
  print("!!!BETTER LUCK NEXT TIME!!!")










  
  
  
  
  
  
  
  
  
  
  

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
