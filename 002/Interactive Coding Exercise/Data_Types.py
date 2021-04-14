# Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8.

two_digit_number = input("Type a two digit number: ")
#print(type(two_digit_number)) # String Datatype

first_digit = two_digit_number[0]
second_digit = two_digit_number[1]

# result = first_digit + second_digit
# print(type(first_digit)) # String Datatype
# result is cancatinated
# if input is 18 then output is 18
# because first_digit and second_digit are also of string data types

result = int(first_digit) + int(second_digit)
print(result)

