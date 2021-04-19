# Loops in Python #
# --------------- #

# loops are used to perform a task multiple times

# For Example:  

# For Loop with Lists: 
fruits = ["Apple", "Peach", "Pear"]

for fruit in fruits:   # puting the elements of fruits in new variable fruit
  print(fruit)
  print(fruit + " Pie")

print(fruits)


# For loop with Range

# range(start, stop[, step])
for number in range(1, 10):
  print(number)
# prints numbers from 1 to 10 but not 10

# to print 10 with that we had to set the range from 1 to 11
for number in range(1, 11):
  print(number)
# prints numbers from 1 to 10

for number in range(1, 11, 3):
  print(number)
# prints number stepus by 3
# 1
# 4
# 7
# 10

for number in range(1, 101):
  total += number
print(total)  
# prints sum of numbers from 1 to 100 :5050
