# Python Lists

# Lists are called a data structure its a way of organising and storing data in python
# We can store multiple data in a single list
# we can store the data of even mix datatypes

# Syntax of list
# List_Name = [Item_1, Item_2, "Item_3", ...]

# For Example: 
# fruits = ["Cherry", "Apple", "Pear"] 

# For Example: 
states_of_america = [
  "Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", 
  "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", 
  "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", 
  "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", 
  "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", 
  "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", 
  "New Mexico", "Arizona", "Alaska", "Hawaii"
]

print(states_of_america)  # print all states

print(states_of_america[2])  # print New Jersey  # Positive Indexing

print(states_of_america[-1])  # print Hawaii  # Negative Indexing

print(states_of_america[-2])  # print Alaska

states_of_america[1] = "Pencilvania"  # update that element

states_of_america.append("Angelaland")  
# append function adds another single item to the end of the list

states_of_america.extend(["Angelaland", "Jack Bauer land"]) 
# extend function adds more then one items to the list

