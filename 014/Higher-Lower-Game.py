from random import randint
from replit import clear
from art import logo, vs
from game_data import data

def random_data():
  random_number = randint(0, 50)
  # print(data[random_number])
  return data[random_number]
score = 0
def check(a, b, option):
  global score
  if option == 'a':
    if a['follower_count'] > b['follower_count']:
      print(logo)
      a = b
      score += 1
      print(f"You're right! Current score: {score}.")
      game(a, b)
    elif a['follower_count'] < b['follower_count']:
      print(logo)
      print(f"Sorry, that's wrong. Final score: {score}")
      return
    else:
      print(logo)
      print(f"Draw! Current score: {score}")
      a = b
      b = random_data()
      game(a, b)
  elif option == 'b':
    if a['follower_count'] < b['follower_count']:
      print(logo)
      a = b
      score += 1
      print(f"You're right! Current score: {score}.")
      game(a, b)
    elif a['follower_count'] > b['follower_count']:
      print(logo)
      print(f"Sorry, that's wrong. Final score: {score}")
      return
    else:
      print(logo)
      print(f"Draw! Current score: {score}")
      a = b
      b = random_data()
      game(a, b)

def game(Compare_A, Against_B):
  print(f"Compare A: {Compare_A['name']}, a {Compare_A['description']}, from {Compare_A['country']}.")
  print(vs)
  print(f"Against B: {Against_B['name']}, a {Against_B['description']}, from {Against_B['country']}.")
  option = input("Who has more followers? Type 'A' or 'B': ").lower()
  clear()
  check(Compare_A, Against_B, option)

print(logo)
Compare_A = random_data()
Against_B = random_data()
game(Compare_A, Against_B)
