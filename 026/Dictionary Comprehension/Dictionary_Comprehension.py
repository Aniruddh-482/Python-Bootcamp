# Dictionary Comprehension

# How to use Dictionary Comprehension.
# With List
# Syntax: 
# new_dict = {new_key:new_value for item in list}

# With Dictionary
# Syntax: 
# new_dict = {new_key:new_value for (key, value) in dict.items()}

# Conditional Dictionary Comprehension
# Syntax: 
# new_dict = {new_key:new_value for (key, value) in dict.items() if test}


# For Example: 
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
import random

# Dictionary Comprehension
students_scores = {student:random.randint(1, 100) for student in names}
print(students_scores)
# Output ==>
# {'Alex': 9, 'Beth': 36, 'Caroline': 49, 'Dave': 91, 'Eleanor': 16, 'Freddie': 46}

# Conditional Dictionary Comprehension
passed_students = {student:score for (student, score) in students_scores.items() if score >= 60}
print(passed_students)
# Output ==>
# {'Dave': 91}
