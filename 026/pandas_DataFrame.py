# How to Iterate over a Pandas DataFrame.

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    print(value)
# Output:
# ['Angela', 'James', 'Lily']
# [56, 76, 98]

import pandas

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)
# Output:
#   student  score
# 0  Angela     56
# 1   James     76
# 2    Lily     98

# Loop through a data frame: 
for (key, value) in student_data_frame.items():
    print(key)
# Output:
# student
# score

for (key, value) in student_data_frame.items():
    print(value)
# Output:
# 0    Angela
# 1     James
# 2      Lily
# Name: student, dtype: object
# 0    56
# 1    76
# 2    98
# Name: score, dtype: int64

# Loop through rows of a data frame:
for (index, row) in student_data_frame.iterrows():
    print(index)
# Output:
# 0
# 1
# 2

for (index, row) in student_data_frame.iterrows():
    print(row)
# Output:
# student    Angela
# score          56
# Name: 0, dtype: object
# student    James
# score         76
# Name: 1, dtype: object
# student    Lily
# score        98
# Name: 2, dtype: object

for (index, row) in student_data_frame.iterrows():
    print(row.student)
# Output: 
# Angela
# James
# Lily

for (index, row) in student_data_frame.iterrows():
    print(row.score)
# Output: 
# 56
# 76
# 98

for (index, row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.score)
# Output: 56

