################### Scope ####################

enemies = 1  # Global Scope

def increase_enemies():
  enemies = 2  # Local Scope
  print(f"enemies inside function: {enemies}")  # Prints 2

increase_enemies()
print(f"enemies outside function: {enemies}")  # Prints 1

# Solution:
enemies = "Skeleton"  # Global Scope  # Variable_01

def increase_enemies():
  enemies = "Zombie"  # Local Scope  # Variable_02
  # Variable_02 is a new and different variable then Variable_01
  print(f"enemies inside function: {enemies}")  # Prints Zombie

increase_enemies()
print(f"enemies outside function: {enemies}")  # Prints Skeleton
# Both the variables of local scope and global scope have same name but are totally different varibles

# Local Scope
# define variables or functions within the function, and only accessible within the function
def drink_potion():
  potion_strength = 2  # local scope
  # only accessible within the function
  print(potion_strength)
drink_potion()  # Prints 2
# print(potion_strength)  # gives error

# Global Scope
# define variables or functions outside the function, and we can use it every whenever we want, it's available anywhere within a file  
player_health = 10  # global scope
def drink_potion():
  potion_strength = 2  # local scope
  print(player_health)  
drink_potion()  # Prints 10
print(player_health)  # Prints 10

# 
enemies = 1  # Global Scope
def increase_enemies():
  print(f"enemies inside function: {enemies}")  # Prints 1

# Local Function
# only available within a function in which it is defined
player_health = 10  
def game():
  def drink_potion():  # local scope/ locaal  function
    potion_strength = 2  
    print(player_health)  
  drink_potion()  # Prints 10
# drink_potion()  # gives error
print(player_health)  # Prints 10  

# Does Python have block scope
# A block scope is the area within if, switch conditions or for and while loops. 
# Generally speaking, whenever you see {curly brackets}, it is a block. 
# to declare variables in the block scope, which means those variables exist only within the corresponding block.
# There is no block scope
game_level =3
enemies = ["Skeleton", "Zombie", "Aliens"]
if game_level < 5:
  new_enemy = enemies[0]
print(new_enemy)  # Prints Skeleton

# but if we put the if statement in a function the variable within the if statement is only available within the function
game_level =3
enemies = ["Skeleton", "Zombie", "Aliens"]
def create_enemy():
  if game_level < 5:
    new_enemy = enemies[0]  
  print(new_enemy)  # Prints Skeleton
# print(new_enemy)  # gives error

# How to Modify Variables with Global Scope
# Modifying Global Scope
enemies = 1  #Global Scope
def increase_enemies():
  # enemies += 1  # gives error
  global enemies
  enemies += 1  
  print(f"enemies inside function: {enemies}")  # Prints 2
increase_enemies()
print(f"enemies outside function: {enemies}")  # Prints 2

# or by using return
enemies = 1
def increase_enemies():
  print(f"enemies inside function: {enemies}")  # Prints 1
  return enemies + 1
enemies = increase_enemies()
print(f"enemies outside function: {enemies}")  # Prints 2

# Python Constants and Global Scope
#Global Constants

PI = 3.14159
URL = "https://www.google.com"
TWITTER_HANDLE = "@yu_angela"


