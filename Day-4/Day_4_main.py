#Randomisation
#Python random module
#https://www.askpython.com/python-modules/python-random-module-generate-random-numbers-sequences
#https://www.khanacademy.org/computing/computer-science/cryptography/crypt/v/random-vs-pseudorandom-number-generators
import random
import my_module

random_integer = random.randint(1, 10)
print(random_integer)


print(my_module.pi)


random_float = random.random()
print(random_float)  #prints between [0, 1)
#never prints 1
#0.0000000... to 0.9999999......

#How to create a random decimal number between 0 and 5?
random_float1 = random.random() * 5
print(random_float1)

#Love Calculator using randomisation
Love_score = random.randint(1, 100)
print(f"Your Love Score is {Love_score}.")


#You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".
import random
random_side = random.randint(0,1)
if random_side == 0:
  print("Tails")
else:
  print("Heads")


#Python Lists
#Lists are called a data structure its a way of organising and storing data in python
#We can store multiple data in a single list
#we can store the data of even mix datatypes
#Syntax of list
#List_Name = [Item_1, Item_2, "Item_3", ...]
#for example
#fruits = ["Cherry", "Apple", "Pear"] 
#Things Lists can do in Python:
#https://docs.python.org/3/tutorial/datastructures.html

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

print(states_of_america)  #print all states
print(states_of_america[2])  #print New Jersey  #Positive Indexing
print(states_of_america[-1])  #print Hawaii  #Negative Indexing
print(states_of_america[-2])  #print Alaska
states_of_america[1] = "Pencilvania"  #update that element
states_of_america.append("Angelaland")  
#append function adds another single item to the end of the list
states_of_america.extend(["Angelaland", "Jack Bauer land"]) 
#extend function adds more then one items to the list

dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]


#You are going to write a program which will select a random name from a list of names. 
#The person selected will have to pay for everybody's food bill.
#Important: You are not allowed to use the choice() function.
#Line 8 splits the string names_string into individual names and puts them inside a List called names.
#For this to work, you must enter all the names as name followed by comma then space. e.g. name, name, name

#split() is basically used to split a string into a list on the basis of the given separator. In our code, the words were separated by spaces. 
#By default, if we do not pass anything to the split() method it splits up the string on the basis of the position of spaces
#Hence though we have not mentioned the separator parameter, the split() method gives us a list of the respective strings

import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

number_of_friends = len(names)
random_friend = random.randint(0, number_of_friends-1)
bill_payer = names[random_friend]
print(bill_payer + " is going to buy the meal today!")
#or
import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
bill_payer = random.choice(names)  #Choice function pick one element of given list
print(bill_payer + " is going to buy the meal today!")











