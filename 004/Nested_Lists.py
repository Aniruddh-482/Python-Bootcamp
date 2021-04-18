# Nested Lists #
# ------------ #

# Nisted Lists: Lists within list

# For Example: 

# dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines",  "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]
print(dirty_dozen)
# prints the two seperate lists within a list
# [['Strawberries', 'Nectarines', 'Apples', 'Grapes', 'Peaches', 'Cherries', 'Pears'], ['Spinach', 'Kale', 'Tomatoes', 'Celery', 'Potatoes']]

print(dirty_dozen[0])
print(dirty_dozen[1])
# ['Strawberries', 'Nectarines', 'Apples', 'Grapes', 'Peaches', 'Cherries', 'Pears']
# ['Spinach', 'Kale', 'Tomatoes', 'Celery', 'Potatoes']

print(dirty_dozen[1][2])
print(dirty_dozen[1][3])
# Tomatoes
# Celery

print(dirty_dozen[0][1])
print(dirty_dozen[1][2])
# Nectarines
# Tomatoes

print(dirty_dozen[1][1])
# Kale
