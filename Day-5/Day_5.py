#Loops in Python
#loops are used to perform a task multiple times
#for Example 
#For Loop with Lists
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:  #puting the elements of fruits in new variable fruit
  print(fruit)
  print(fruit + " Pie")
print(fruits)
#Output==>
# Apple
# Apple Pie
# Peach
# Peach Pie
# Pear
# Pear Pie
# ['Apple', 'Peach', 'Pear']


#len() function gives the total numbers of elements are in list
#sum() function adds all the elements in the list

# You are going to write a program that calculates the average student height from a List of heights.
# without using len() and sum()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

number_of_students = 0
sum_of_heights = 0
for height in student_heights:
  sum_of_heights += height
  number_of_students += 1

average_height = sum_of_heights / number_of_students
average_as_int = round(average_height)
print(average_as_int)
# Output==>
# Input a list of student heights 24 59 68
# 50


# max() prints maximum element in the given list
# min() prints minimum element in the given list

# You are going to write a program that calculates the highest score from a List of scores.
# Without using max() and min()
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
highest_score = 0
for score in student_scores:
  if score > highest_score:
    highest_score = score
print(f"The highest score in the class is: {highest_score}")


# For loop with Range
# range(start, stop[, step])
for number in range(1, 10):
  print(number)
# prints numbers from 1 to 10 but not 10
# to print 10 with that we had to set the range from 1 to 11
for number in range(1, 11):
  print(number)
# prints numbers from 1 to 10
for number in range(1, 11, 3):
  print(number)
# prints number stepus by 3
# 1
# 4
# 7
# 10
for number in range(1, 101):
  total += number
print(total)  #prints sum of numbers from 1 to 100 :5050

# You are going to write a program that calculates the sum of all the even numbers from 1 to 100. Thus, the first even number would be 2 and the last one is 100:
total = 0
for number in range(1, 101):
  if number % 2 == 0:
    total += number
print(total)
# or
total = 0
for number in range(1, 101, 2):
  total += number
print(total)
# prints sum of all even numbers from 1 to 100 : 2550


# You are going to write a program that automatically prints the solution to the FizzBuzz game.
# Your program should print each number from 1 to 100 in turn.
# When the number is divisible by 3 then instead of printing the number it should print "Fizz".
# When the number is divisible by 5, then instead of printing the number it should print "Buzz".
# And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz".
for number in range(1, 101):
  if number % 3 == 0 and number % 5 ==0:  #Divisible by both 3 and 5
    print("FizzBuzz")
  elif number % 3 == 0:  #Divisible by 3
    print("Fizz")
  elif number % 5 == 0:  #Divisible by 5
    print("Buzz")
  else:
    print(number) 


# Create a Password Generator
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password = ""
for char in range(1, nr_letters + 1):
  # random_char = random.choice(letters)
  # # print(random_char)
  # password = password + random_char
  # print(password)
  password += random.choice(letters)
for char in range(1, nr_symbols + 1):
  password += random.choice(symbols)
for char in range(1, nr_numbers + 1):
  password += random.choice(numbers)
print(password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password_list = []
for char in range(1, nr_letters + 1):
  password_list.append(random.choice(letters))
for char in range(1, nr_symbols + 1):
  password_list += random.choice(symbols)
for char in range(1, nr_numbers + 1):
  password_list += random.choice(numbers)
# print(password_list)
random.shuffle(password_list)
# print(password_list)
password = ""
for char in password_list:
  password += char
print(f"Your Password is: {password}")




