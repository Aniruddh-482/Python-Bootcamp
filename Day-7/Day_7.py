# Hangman Game Project
# Step_01
#Picking a random word and checking answers
#How to check user's answer
import random
word_list = ["aardvark", "baboon", "camel"]
letter = input("Guess a letter: ")
random_number = random.randint(0, 2)
# print(word_list[random_number])
for letters in word_list[random_number]:
    if letters == letter:
        print("Right")
    else:
        print("Wrong")
# or
# Picking a random word and checking answers
import random
word_list = ["aardvark", "baboon", "camel"]
#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
random_number = random.randint(0, 2)
chosen_word = word_list[random_number]
guess = input("Guess a letter: ")
guess = guess.lower()
print(chosen_word)
for letters in chosen_word:
    if letters == guess:
        print("Right")
    else:
        print("Wrong")
# How to check user's answer
# Solution of Step_01: 
word_list = ["aardvark", "baboon", "camel"]
#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
import random
chosen_word = random.choice(word_list)
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Guess a letter: ").lower()
#TODO-3 - Check if the letter the user guessed (guess) is one of the leters in the chosen_word.
for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")

# Step_02
# Replacing blanks with guesses
import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
#Testing code
print(f'Pssst, the solution is {chosen_word}.')
#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
display = []
guess = input("Guess a letter: ").lower()
count = len(chosen_word)
display.insert(0, '_')
for num in range(count - 1):
    display.append('_')
#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
num = 0
for letter in chosen_word:
    num += 1
    if letter == guess:
        display[num - 1] = guess
#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
print(display)
# How to replace Blanks
# Solution of Step_02:
import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
#Testing code
print(f'Pssst, the solution is {chosen_word}.')
#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"
guess = input("Guess a letter: ").lower()
#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
for position in range(word_length):
    letter = chosen_word[position]
    #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
    if letter == guess:
        display[position] = letter
#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
print(display)
 
