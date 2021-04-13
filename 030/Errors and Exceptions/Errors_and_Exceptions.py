# Handling Errors and Exceptions

# FileNotFound
# with open("a_file.txt") as file:
#     file.read()

# KeyError
# a_dictionary = {"key": "value"}
# value = a_dictionary["non_existent_key"]

# IndexError
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]

# TypeError
# text = "abc"
# print(text + 5)


# Catching Exceptions:

# try: Something that might cause an exception.
# except: Do this if there was an exception.
# else: Do this if there was no exception.
# finally: Do this no matter what happens.

# FileNotFound
# with open("a_file.txt") as file:
#     file.read()

# Solution:

try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["non_existent_key"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Something")
except KeyError as error_message:
    print(f"That key {error_message} does not exist.")
else:  # Occur only when there is no error in try
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed.")


# Raising Expression

# For Example:
# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["non_existent_key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"That key {error_message} does not exist.")
# else:  # Occur only when there is no error in try
#     content = file.read()
#     print(content)
# finally:
#     raise TypeError("This is an error that I made up.")

# For Example:
height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human Height should not be over 3 meters.")

bmi = weight / height ** 2
print(bmi)

