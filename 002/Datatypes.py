# Data Types
# Strings
print("Hello"[0])
print("Hello"[4])

# numbers between double quotes are treated as strings
# for example
print("123"+"356")

# Integer
print(123+345)
# 123456789 and 123_456_789 are treated same

# float(Floating point number)
3.14159

# Boolean
True
False

# Type Error
# len(1234) gives an error(TypeError)
# we can only cancatinate string to string (not string to int)
# for example: 
num_char = len(input("What is your name: "))
# print("Your name has "+num_char+" characters.") 
# it gives error

# Type Checking
print(type(num_char)) # type function checks datatype of variable
new_num_char = str(num_char)
print(type(new_num_char))
print("Your name has "+new_num_char+" characters.") 

# Type Conversion
a = 123
print(a)
print(type(a))  # Integer

a = str(123)
print(a)
print(type(a))  # String

a = float(123)
print(a)
print(type(a))  # Float

print(70 + float("100.5")) # Result = 170.5
print(str(70) + str(100)) # Result = 70100
