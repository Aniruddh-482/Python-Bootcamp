# List Comprehension
# How to Create Lists using List Comprehension.
# Syntax: 
# new_list = [new_item for item in list]

# For Lists
# For Example: 
numbers = [1, 2, 3]
# Creating new list using for loop.
new_numbers = []
for n in numbers:
	add_1 = n + 1
	new_numbers.append(add_1)
# Creating new list using List Comprehension.
new_numbers = [n + 1 for n in numbers]
print(new_numbers)
# Output ==> [2, 3, 4]

# For Strings
# We can also use List Comprehension on strings
# For Example: 
name = "Angela"
new_list = [letter for letter in name]
print(new_list)
# Output ==> ['A', 'n', 'g', 'e', 'l', 'a']

# Python Sequences:
# They have a specific order and they work through that sequence.
# > Lists
# > Range
# > Strings
# > Tuples

# For Range
# For Example:
range_list = [num * 2 for num in range(1, 5)]
print(range_list)
# Output ==> [2, 4, 6, 8]

# Conditional List Comprehension
# Syntax: 
# new_list = [new_item for item in list if test]

# For Example:
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
print(short_names)
# Output ==> ['Alex', 'Beth', 'Dave']

# For Example:
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
long_names = [name.upper() for name in names if len(name) > 5]
print(long_names)
# Output ==> ['CAROLINE', 'ELEANOR', 'FREDDIE']

