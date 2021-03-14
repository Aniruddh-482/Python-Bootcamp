# The Python Dictionary
# Dictionaries are Python’s implementation of a data structure that is more generally known as an associative array. 
# A dictionary consists of a collection of key-value pairs. 
# Each key-value pair maps the key to its associated value.
# Syntax of Dictionary:
# {Key: Value}
# For Example:
# programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected."}
# You can add more keys and values by using ", "
# programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", "Function": "A piece of code that you can easily call over and over again.", "Loop":"The action of doing something over and over again"}
# or
programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.", 
  "Function": "A piece of code that you can easily call over and over again.", 
  "Loop":"The action of doing something over and over again.",
}
# Retrieving items from Dictionary
# To select a element in Dictionary we had to use its key
# for example
print(programming_dictionary["Bug"])  #Prints its value
# An error in a program that prevents the program from running as expected.

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

# Retrieving items from Dictionary
print(programming_dictionary["Bug"])  

# Adding new items to Dictionary.
programming_dictionary["Loop"] = "The action of doing something over and over again."
print(programming_dictionary)

# Creat an empty Dictionary
empty_dictionary = {}

# Wipe an existing Dictionary
programming_dictionary = {}
print(programming_dictionary)

# Edit an item in a Dictionary
programming_dictionary["Bug"] = "A moth in your Computer."
print(programming_dictionary)

# Loop through a Dictionary
# for thing in programming_dictionary:
#     print(thing) 
# Output ==> print all the keys 
# Bug
# filter
# Loop
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
# Output ==> print all the keys 
# Bug
# A moth in your Computer.
# Function
# A piece of code that you can easily call over and over again.
# Loop
# The action of doing something over and over again.


# Grading Program
# Instructions
# You have access to a database of student_scores in the format of a dictionary. 
# The keys in student_scores are the names of the students and the values are their exam scores.
# Write a program that converts their scores to grades. 
# By the end of your program, you should have a new dictionary called student_grades that should contain student names for keys and their grades for values. 
# The final version of the student_grades dictionary will be checked.
# DO NOT modify lines 1-7 to change the existing student_scores dictionary.
# DO NOT write any print statements.
# This is the scoring criteria:
# Scores 91 - 100: Grade = "Outstanding"
# Scores 81 - 90: Grade = "Exceeds Expectations"
# Scores 71 - 80: Grade = "Acceptable"
# Scores 70 or lower: Grade = "Fail"
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}
#TODO-2: Write your code below to add the grades to student_grades.
for key in student_scores:
    if student_scores[key] > 90:
        student_grades[key] = "Outstanding"
    elif student_scores[key] > 80:
        student_grades[key] = "Exceeds Expectations"
    elif student_scores[key] > 70:
        student_grades[key] = "Acceptable"
    elif student_scores[key] <= 70:
        student_grades[key] = "Fail"
print(student_grades)
# or
#TODO-2: Write your code below to add the grades to student_grades.
for student in student_scores:
    score = student_score[student]
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Exceeds Expectations"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"
print(student_grades)


# Nesting Lists and Dictionaries
# {
#   Key: [List],
#   Key2: {Dict},
# }
#Nesting 
capitals = {
  "France": "Paris",
  "Germany": "Berlin",
}

#Nesting a List in a Dictionary
# {[], []}
travel_log = {
  "France": ["Paris", "Lille", "Dijon"],
  "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

#Nesting Dictionary in a Dictionary
# {{}, {}}
travel_log = {
  "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
  "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
}

#Nesting Dictionaries in Lists
[{}, {}]
travel_log = [
{
  "country": "France", 
  "cities_visited": ["Paris", "Lille", "Dijon"], 
  "total_visits": 12,
},
{
  "country": "Germany",
  "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
  "total_visits": 5,
},
]


# Dictionary in List
# Instructions
# You are going to write a program that adds to a travel_log. You can see a travel_log which is a List that contains 2 Dictionaries.
# Write a function that will work with the following line of code on line 21 to add the entry for Russia to the travel_log.
# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# You've visited Russia 2 times.
# You've been to Moscow and Saint Petersburg.
# DO NOT modify the travel_log directly. You need to create a function that modifies it.
travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#TODO: Write the function that will allow new countries
#to be added to the travel_log. 
def add_new_country(country, visits, cities):
    updated_travel_log = {
        "country": country,
        "visits": visits,
        "cities": cities,
    }
    travel_log.append(updated_travel_log)
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
# or
#TODO: Write the function that will allow new countries
#to be added to the travel_log.
def add_new_country(name, visit_count, cities_visited):
  new_country = {}
  new_country["country"] = name
  new_country["visits"] = visit_count
  new_country["cities"] = cities_visited
  travel_log.append(new_country)
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)



