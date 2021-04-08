# List Comprehension 2
# -------------------- #
# Instructions: 
# You are going to write a List Comprehension to create a new list called result. 
# This new list should only contain the even numbers from the list numbers.

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

result = [num for num in numbers if num % 2 == 0]

print(result)

# Output ==>
# [2, 8, 34]

