# Write a program for a treasure game. 

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

option_1 = input('You are at a cross road. where do you want to go? type "left" or "right" ')

if option_1 == "left":
  option_2 = input('You come to a lake. There is an island in the middle of the lake. type "wait" to wait for a boat or type "swim" to swim across. ')
  if option_2 == "wait":
    option_3 = input('You arive at the island unharmed.There is a house with Three doors. One red, one yellow, and one blue. Which colour do you choose? ')
    if option_3 == "yellow":
      print("!!!!!!!Congatulations you found the HIDDEN Treasure!!!!!!!")
      print("YOU WIN!")
      print("GAME OVER!")
    elif option_3 == "red":
      print("YOU BURNED BY FIRE")
      print("GAME OVER!")
      print("!!!BETTER LUCK NEXT TIME!!!")
    elif option_3 == "blue":
      print("YOU ENTERED IN THE ROOM OF BEASTS")
      print("GAME OVER!")
      print("!!!BETTER LUCK NEXT TIME!!!")
    else:
      print("!!!GAME OVER!!!")
  else:
    print("YOU ATTACKED BY A GROUP OF SHARKS IN THE LAKE")
    print("GAME OVER!")
    print("!!!BETTER LUCK NEXT TIME!!!")
else:
  print("YOU HAD AN ACCIDENT AND DIED!!")
  print("GAME OVER!")
  print("!!!BETTER LUCK NEXT TIME!!!")
