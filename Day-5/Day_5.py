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





