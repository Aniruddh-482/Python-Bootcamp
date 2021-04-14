# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

bmi = int(weight) / float(height) ** 2  # Float Datatype

bmi_as_int = int(bmi)

print(bmi_as_int)

