# Hangman Game Project #
# -------------------- #

# Step_01
# Picking a random word and checking answers
# How to check user's answer

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.


# Step_02
# Replacing blanks with guesses

# TODO-1: - Create an empty List called display.
    # For each letter in the chosen_word, add a "_" to 'display'.
    # So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
# TODO-2: - Loop through each position in the chosen_word;
    # If the letter at that position matches 'guess' then reveal that letter in the display at that position.
    # e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
# TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
    # Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.


# Step_03
# Checking if the player has won

# TODO-1: - Use a while loop to let the user guess again. 
    # The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). 
    # Then you can tell the user they've won.)


# Step_04
# Keeping track of player's lives

# TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. 
    # Set 'lives' to equal 6.
# TODO-2: - If guess is not a letter in the chosen_word,
    # Then reduce 'lives' by 1. 
    # If lives goes down to 0 then the game should stop and it should print "You lose."
# TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.


# Step_05
# Improving the User Experience

# TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
    # Delete this line: word_list = ["ardvark", "baboon", "camel"]
# TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
# TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
# TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
# TODO-2: - Import the stages from hangman_art.py and make this error go away.


# Final Hangman Game #

import random
from hangman_art import stages, logo
from hangman_words import word_list
from replit import clear
print(logo)
game_is_finished = False
lives = len(stages) - 1
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
display = []
for _ in range(word_length):
    display += "_"
while not game_is_finished:
    guess = input("Guess a letter: ").lower()
    # Use the clear() function imported from replit to clear the output between guesses.
    clear()
    if guess in display:
        print(f"You've already guessed {guess}")
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(f"{' '.join(display)}")
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            game_is_finished = True
            print("You lose.")
            print(f"The correct word is {chosen_word}")
    if not "_" in display:
        game_is_finished = True
        print("You win.")
    print(stages[lives])
