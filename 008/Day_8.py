# Function Parameters
# Functions with Inputs
# def my_function(something):  # Something = 123
	# Do this with something   #    |         |
	# Then do this             # Parameter   Argument
	# Finally do this
# my_function(123)  #or any data you want to pass to my_function
# Argument is actual piece of data thts going to be passed over to the function when its being called
# Parameter is the name of that data and we use the parameter inside the function to refer to it and do things with it

# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.
# Simple Function
def greet():
    print("Hello")
    print("How do you do?")
    print("Isn't the weather nice today?")
greet()
# With Inputs or With Parameters
# Function that allows for input
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")
    print("Isn't the weather nice today?")
greet_with_name("Ansh")

#Functions with more than 1 input
def greet_with(name, location):
  print(f"Hello {name}")
  print(f"What is it like in {location}?")
#Calling greet_with() with Positional Arguments
greet_with("Jack Bauer", "Nowhere")
#vs.
greet_with("Nowhere", "Jack Bauer")
#Calling greet_with() with Keyword Arguments
greet_with(location="London", name="Angela")
# 
greet_with("Ansh", "Ujjain")  # Positional Argument
greet_with(location = "Ujjain", name = "Ansh")  # Keyword Argument


# Area Calculation Exercise
# You are painting a wall. The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall. 
# Given a random height and width of wall, calculate how many cans of paint you'll need to buy.
# number of cans = (wall height ✖️ wall width) ÷ coverage per can.
# e.g. Height = 2, Width = 4, Coverage = 5
# number of cans = (2 ✖️ 4) ÷ 5
#                      = 1.6
#                      = 1.6
# But because you can't buy 0.6 of a can of paint, the result should be rounded up to 2 cans.
import math
def paint_calc(height, width, cover):
    number_of_cans = math.ceil(height * width / cover)
    print(f"You'll need {number_of_cans} cans of paint.")
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
# or
import math
def paint_calc(height, width, cover):
	area = height * width
	num_of_cans = math.ceil(area / cover)
    print(f"You'll need {num_of_cans} cans of paint.")
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)


# Prime Number Checker
# Prime Numbers
# Instructions
# Prime numbers are numbers that can only be cleanly divided by itself and 1.
# https://en.wikipedia.org/wiki/Prime_number
# You need to write a function that checks whether if the number passed into it is a prime number or not.
def prime_checker(number):
    flag = 0
    for num in range(2, number):
        if number % num == 0:
            flag = 1
    if flag == 0:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")
n = int(input("Check this number: "))
prime_checker(number=n)
# or
def prime_checker(number):
	is_prime = True
	for i in range(2, number):
		if number % i == 0:
			is_prime = False
	if is_prime:
		print("It's a prime number.")
    else:
        print("It's not a prime number.")
n = int(input("Check this number: "))
prime_checker(number=n)


# Caesar Cipher Project 
# Caesar Cipher Part 1 - Encryption
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(plain_text, shift_amount):
    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"The encoded text is {cipher_text}")
    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list
    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛
    ##Solved by joust copying and pasting the elements of alphabet again in it #index function only gives the first index value of element it found in given list
#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
encrypt(plain_text=text, shift_amount=shift)

# Caesar Cipher Part 2 - Decryption
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        cipher_text += alphabet[new_position]
    print(f"The encoded text is {cipher_text}")
#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def decrypt(cipher_text, shift_amount):
    #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
    #e.g. 
    #cipher_text = "mjqqt"
    #shift = 5
    #plain_text = "hello"
    #print output: "The decoded text is hello"
    plain_text = ""
    for letter in cipher_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        plain_text += alphabet[new_position]
    print(f"The encoded text is {plain_text}")
#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.
if direction == "encode":
    encrypt(plain_text=text, shift_amount=shift)
elif direction == "decode":
    decrypt(cipher_text=text, shift_amount=shift)

# Caesar Cipher Part 3 - Reorganising our Code
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 
def caesar(text, shift, direction):
  new_text = ""
  for letter in text:
    position = alphabet.index(letter)
    if direction == "encode":
        new_position = position + shift
    elif direction == "decode":
        new_position = position - shift
    new_text += alphabet[new_position]
  print(f"The encoded text is {new_text}")
#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
caesar(text=text, shift=shift, direction=direction)
# or
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 
def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
      shift_amount *= -1
  for letter in start_text:
    position = alphabet.index(letter)
    new_position = position + shift_amount
    end_text += alphabet[new_position]
  print(f"Here's the {direction} result: {end_text}")
#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

# Caesar Cipher Part 4 - User Experience Improvements and Final Touches
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    #TODO-3: What happens if the user enters a number/symbol/space?
    #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
    #e.g. start_text = "meet me at 3"
    #end_text = "•••• •• •• 3"
    if char in alphabet:
        position = alphabet.index(char)
        new_position = position + shift_amount
        end_text += alphabet[new_position]
    else:
        end_text += char
  print(f"Here's the {cipher_direction}d result: {end_text}")
#TODO-1: Import and print the logo from art.py when the program starts.
from art import logo
print(logo)
#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.
choice = "yes"
while choice == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    #TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
    #Try running the program and entering a shift number of 45.
    #Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
    #Hint: Think about how you can use the modulus (%).
    if shift > 25:
        shift = shift % 26
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    choice = input("Want to restart the program? Type 'yes' or 'no': ")
# or
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    #TODO-3: What happens if the user enters a number/symbol/space?
    #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
    #e.g. start_text = "meet me at 3"
    #end_text = "•••• •• •• 3"
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:
      end_text += char
  print(f"Here's the {cipher_direction}d result: {end_text}")
#TODO-1: Import and print the logo from art.py when the program starts.
from art import logo
print(logo)
#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.
should_end = False
while not should_end:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  #TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
  #Try running the program and entering a shift number of 45.
  #Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
  #Hint: Think about how you can use the modulus (%).
  shift = shift % 26
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
  restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if restart == "no":
    should_end = True
    print("Goodbye")


