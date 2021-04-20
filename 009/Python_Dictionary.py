# The Python Dictionary #
# --------------------- #

# Dictionaries are Python’s implementation of a data structure that is more generally known as an associative array. 
# A dictionary consists of a collection of key-value pairs. 
# Each key-value pair maps the key to its associated value.

# Syntax of Dictionary:
# {Key: Value}

# For Example:
# programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected."}

# You can add more keys and values by using ", "
programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.", 
  "Function": "A piece of code that you can easily call over and over again.", 
}

# Retrieving items from Dictionary
# To select a element in Dictionary we had to use its key

# For Example: 
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

for thing in programming_dictionary:
    print(thing) 
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


# Nesting Lists and Dictionaries #
# ------------------------------ #

# Nesting 
# {
#   Key: [List],
#   Key2: {Dict},
# }

# For Example: 
capitals = {
  "France": "Paris",
  "Germany": "Berlin",
}

# Nesting a List in a Dictionary
# {[], []}
travel_log = {
  "France": ["Paris", "Lille", "Dijon"],
  "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

# Nesting Dictionary in a Dictionary
# {{}, {}}
travel_log = {
  "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
  "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
}

# Nesting Dictionaries in Lists
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

