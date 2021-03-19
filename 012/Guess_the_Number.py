########## The Number Guessing Game ##########

# Number Guessing Game Objectives:
# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
from art import my_logo

def game(lives, random_number):
  if not lives == 0:
    guess = int(input("Make a guess: "))
    if random_number == guess:
      print(f"You got it! The answer was {guess}.")
      return
    elif guess < random_number:
      lives -= 1
      print("Too low.")
      print("Guess again.")
      print(f"You have {lives} attempts remaining to guess the number.")
      game(lives, random_number)
    elif guess > random_number:
      lives -= 1
      print("Too high.")
      print("Guess again.")
      print(f"You have {lives} attempts remaining to guess the number.")
      game(lives, random_number)
  else:
    print("Too low.")
    print("You've run out of guesses, you lose.")

print(my_logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
random_number = random.randint(1, 101)
print(f"Pssst, the correct answer is {random_number}")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
difficulty.lower()
end_of_game = False
if  difficulty == "easy":
  print("You have 10 attempts remaining to guess the number.")
  lives = 10
  game(lives, random_number)
elif difficulty == "hard":
  print("You have 5 attempts remaining to guess the number.")
  lives = 5
  game(lives, random_number)

  
  
