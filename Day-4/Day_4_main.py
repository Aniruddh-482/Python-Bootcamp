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




















