# You are going to write a program that calculates the average student height from a List of heights.

# NOTE: without using len() and sum()

student_heights = input("Input a list of student heights: ").split()

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
