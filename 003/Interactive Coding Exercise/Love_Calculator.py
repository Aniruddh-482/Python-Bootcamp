# The lower() function changes all the letters in a string to lower case.
# https://stackoverflow.com/questions/6797984/how-do-i-lowercase-a-string-in-python

# The count() function will give you the number of times a letter occurs in a string.
# https://stackoverflow.com/questions/1155617/count-the-number-occurrences-of-a-character-in-a-string

# You are going to write a program that tests the compatibility between two people. 
# We're going to use the super scientific method recommended by BuzzFeed.
# To work out the love score between two people:
# Take both people's names and check for the number of times the letters in the word TRUE occurs. 
# Then check for the number of times the letters in the word LOVE occurs. 
# Then combine these numbers to make a 2 digit number.

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

small_name1 = name1.lower()
small_name2 = name2.lower()

t_count_name1 = small_name1.count("t")
r_count_name1 = small_name1.count("r")
u_count_name1 = small_name1.count("u")
e_count_name1 = small_name1.count("e")

true_count_name1 = t_count_name1 + r_count_name1 + u_count_name1 + e_count_name1

l_count_name1 = small_name1.count("l")
o_count_name1 = small_name1.count("o")
v_count_name1 = small_name1.count("v")
e_count_name1 = small_name1.count("e")

love_count_name1 = l_count_name1 + o_count_name1 + v_count_name1 + e_count_name1

t_count_name2 = small_name2.count("t")
r_count_name2 = small_name2.count("r")
u_count_name2 = small_name2.count("u")
e_count_name2 = small_name2.count("e")

true_count_name2 = t_count_name2 + r_count_name2 + u_count_name2 + e_count_name2

l_count_name2 = small_name2.count("l")
o_count_name2 = small_name2.count("o")
v_count_name2 = small_name2.count("v")
e_count_name2 = small_name2.count("e")

love_count_name2 = l_count_name2 + o_count_name2 + v_count_name2 + e_count_name2

total_true_count = true_count_name1 + true_count_name2
total_love_count = love_count_name1 + love_count_name2

total_score = str(total_true_count) + str(total_love_count)
score_as_int = int(total_score)

if score_as_int < 10 or score_as_int > 90:
  print(f"Your score is {score_as_int}, you go together like coke and mentos.")
elif score_as_int > 40 and score_as_int < 50:
  print(f"Your score is {score_as_int}, you are alright together.")
else:
  print(f"Your score is {score_as_int}.")  
 
