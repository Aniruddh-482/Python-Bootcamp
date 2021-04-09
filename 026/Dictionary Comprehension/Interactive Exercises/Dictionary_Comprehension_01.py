# Dictionary Comprehension 1
# -------------------------- #
# Instructions: 
# You are going to use Dictionary Comprehension to create a dictionary called result
# that takes each word in the given sentence and calculates the number of letters in each word.
# Try Googling to find out how to convert a sentence into a list of words.

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

words = sentence.split()

result = {word:len(word) for word in words}

print(result)

# Solution:

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

result = {word:len(word) for word in sentence.split()}

print(result)

# Output == >
# {'What': 4, 'is': 2, 'the': 3, 'Airspeed': 8, 'Velocity': 8, 'of': 2, 'an': 2, 'Unladen': 7, 'Swallow?': 8}
