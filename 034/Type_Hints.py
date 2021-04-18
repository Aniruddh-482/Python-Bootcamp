# Python Typing: Type Hints and Arrows ->

# Declaring Datatypes of variables
age: int
name: str
height: float
is_human: bool


# Declaring Datatypes of variables in function
# and returntype of function

# For Example:
# Declaring age int datatype (Declaring the datatype for a variable)
#                  \   Declaring output of function police_check() bollean datatype (Declaring the datatype for the returntype of a function)
#                   \         /
def police_check(age: int) -> bool:  # Specifying datatype of variable age and output of function police_check()
	if age > 18:
		can_drive = True
	else:
		can_drive = False
	return can_drive

if police_check(12):
	print("You may pass.")
else:
	print("Pay a fine.")


# Type Hints #
# ---------- #

# For Example:
def greetings(name: str) -> str:
	return "Hello" + name

greetings("Aniruddh")
