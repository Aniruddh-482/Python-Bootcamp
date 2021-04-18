# You are going to write a program which will select a random name from a list of names. 
# The person selected will have to pay for everybody's food bill.

# Important: You are not allowed to use the choice() function.
# Line 8 splits the string names_string into individual names and puts them inside a List called names.
# For this to work, you must enter all the names as name followed by comma then space. e.g. name, name, name

# split() is basically used to split a string into a list on the basis of the given separator. In our code, the words were separated by spaces. 
# By default, if we do not pass anything to the split() method it splits up the string on the basis of the position of spaces
# Hence though we have not mentioned the separator parameter, the split() method gives us a list of the respective strings

import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

bill_payer = random.choice(names)  # Choice function pick one element of given list

print(bill_payer + " is going to buy the meal today!")

