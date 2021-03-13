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



