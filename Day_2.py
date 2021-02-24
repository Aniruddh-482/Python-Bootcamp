#Data Types
#Strings
print("Hello"[0])
print("Hello"[4])

#numbers between double quotes are treated as strings
#for example
print("123"+"356")

#Integer
print(123+345)
#123456789 and 123_456_789 are treated same

#float(Floating point number)
3.14159

#Boolean
True
False

#len(1234) gives an error(TypeError)
#we can only cancatinate string to string (not string to int)
#for example
num_char = len(input("What is your name: "))
#print("Your name has "+num_char+" characters.") 
#it gives error 
print(type(num_char)) #type function checks datatype of variable
new_num_char = str(num_char)
print(type(new_num_char))
print("Your name has "+new_num_char+" characters.") 

a = 123
print(a)
print(type(a))

a = str(123)
print(a)
print(type(a))

a = float(123)
print(a)
print(type(a))

print(70 + float("100.5")) #Result = 170.5
print(str(70) + str(100)) #Result = 70100

#Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8
two_digit_number = input("Type a two digit number: ")
#print(type(two_digit_number)) #string datatype
first_digit = two_digit_number[0]
second_digit = two_digit_number[1]
#result = first_digit + second_digit
#print(type(first_digit)) #string datatype
#result is cancatinated
#if input is 18 then output is 18
#because first_digit and second_digit are also of string data types
#so
result = int(first_digit) + int(second_digit)
print(result)

#Mathematical Operations in Python
#'+' Addition
3 + 5
#'-' Substraction
7 - 4
#'*' Multiplicaton
3 * 2
#'/' Division
6 / 3 #it always print a floating point number
#for example print(type(6 / 3)) prints 2.0
#'**' Exponential
2 ** 2 #print(2 ** 2) prints 4
#Python follows PEMDAS
#PEMDAS
#Parentheses ()
#Exponents **
#Multiplicaton *
#Division /
#Addition +
#Substraction -
#Order goes from left to right
#PEMDASLR
#()
#**
#* /
#+ -
#Example print(3 * 3 + 3 / 3 - 3) prints 7

#Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
bmi = int(weight) / float(height) ** 2
bmi_as_int = int(bmi)
print(bmi_as_int)

#Number Manipulation
#round function
print(int(8 / 3)) #prints 2
print(round(8 / 3)) #prints 3
#round function rounds (8 / 3) into a whole number and 2.6 is written as 3
print(round(8 / 3, 2)) #rund it to decimal places 
#prints 2.67
print(round(2.6666666666, 2))
#prints 2.67    

#Flow division //
print(8 // 3) #prints 2 without converting into integer
print(type(8 // 3)) #prints integer datatype
print(type(8 / 3)) #prints float datatype

#Shorthands
#a += b #a = a + b
#a -= b #a = a - b
#a *= b #a = a * b
#a /= b #a = a / b

#F-Strings in Python
#Helps to print data of different datatypes together using single print statement
#for example
score = 0
isheight = 1.78
iswinning = True
#f-String
print(f"Your score is {score}, Your height is {isheight}, you are winning is {iswinning}")

#Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.
age = input("What is your current age?")
age_as_int = int(age)

years_remaining = 90 - age_as_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

#print(f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left.")
#or
message = f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left."
print(message)

#create a tip calculator which takes bill, percentage of tip, and number of persons to pay and give amount each would pay
print("Welcome to the tip calculator!")
bill = input("What was the total bill? ")
bill_as_float = float(bill)
tip_percentage = input("What percentage tip would you like to give? 10, 12, or 15? ")
percent_as_float = float(tip_percentage)
percent = percent_as_float / 100
percent += 1
total_bill = bill_as_float * percent
number_of_persons = input("How many people to split the bill? ")
each_pay = round(total_bill / int(number_of_persons), 2)
message = f"Each person should pay: {each_pay}"
print(message)

