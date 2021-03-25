from replit import clear
logo_1 ="""
                         ad88    ad88                       
                        d8"     d8"                         
                        88      88                          
 ,adPPYba,  ,adPPYba, MM88MMM MM88MMM ,adPPYba,  ,adPPYba,  
a8"     "" a8"     "8a  88      88   a8P_____88 a8P_____88  
8b         8b       d8  88      88   8PP""""""" 8PP"""""""  
"8a,   ,aa "8a,   ,a8"  88      88   "8b,   ,aa "8b,   ,aa  
 `"Ybbd8"'  `"YbbdP"'   88      88    `"Ybbd8"'  `"Ybbd8"'  
"""
logo_2 ="""
                        (
                          )     (
                   ___...(-------)-....___
               .-""       )    (          ""-.
         .-'``'|-._             )         _.-|
        /  .--.|   `""---...........---""`   |
       /  /    |                             |
       |  |    |                             |
        \  \   |                             |
         `\ `\ |                             |
           `\ `|                             |
           _/ /\                             /
          (__/  \                           /
       _..---""` \                         /`""---.._
    .-'           \                       /          '-.
   :               `-.__             __.-'              :
   :                  ) ""---...---"" (                 :
    '._               `"--...___...--"`              _.'
      \""--..__                              __..--""/
       '._     ""-----.....______.....-----""     _.'
          `""--..,,_____            _____,,..--""`
                        `""------""`
"""

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

MONEY = 0
should_continue = True


def resource_modify(coffee_type):
    global MONEY
    MONEY += MENU[coffee_type]["cost"]
    resources["water"] -= MENU[coffee_type]["ingredients"]["water"]
    resources["milk"] -= MENU[coffee_type]["ingredients"]["milk"]
    resources["coffee"] -= MENU[coffee_type]["ingredients"]["coffee"]
    print(f"Here is your {coffee_type} ☕ Enjoy!")


def report(resources):
    global MONEY
    print(f"Water: {resources['water']}")
    print(f"Milk: {resources['milk']}")
    print(f"Coffee: {resources['coffee']}")
    print(f"Money: {MONEY}")


def check_ingredients(coffe_type):
    if resources["water"] >= MENU[coffe_type]["ingredients"]["water"]:
        if resources["milk"] >= MENU[coffe_type]["ingredients"]["milk"]:
            if resources["coffee"] >= MENU[coffe_type]["ingredients"]["coffee"]:
                return True
            else:
                print("Sorry there is not enough coffee.")
                return False
        else:
            print("Sorry there is not enough milk.")
            return False
    else:
        print("Sorry there is not enough water.")
        return False


def coins(coffee_type):
    if check_ingredients(coffee_type):
        print("Please insert coins.")
        quarters = int(input("How many Quarters?: "))
        dimes = int(input("How many Dimes?: "))
        nickles = int(input("How many Nickles?: "))
        pennies = int(input("How many Pennies?: "))
        change = ((quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)) - MENU[coffee_type]["cost"]
        if change >= 0:
            print(f"Here is {change} in change.")
            resource_modify(coffee_type)
        elif change < 0:
            print("Sorry that's not enough money. Money Refunded.")

print(logo_1)
print(logo_2)
while should_continue:
    coffee_type = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if coffee_type == "report":
        clear()
        print(logo_1)
        report(resources)
    elif coffee_type == "off":
        clear()
        print(logo_1)
        print(logo_2)
        should_continue = False
    else:
        clear()
        print(logo_1)
        coins(coffee_type)
