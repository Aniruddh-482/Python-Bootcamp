# Create a tip calculator which takes bill, percentage of tip, and number of persons to pay and give amount each would pay

print("Welcome to the tip calculator!")
bill = input("What was the total bill? ")
bill_as_float = float(bill)
tip_percentage = input("What percentage tip would you like to give? 10, 12, or 15? ")
percent_as_float = float(tip_percentage)
percent = percent_as_float / 100
percent += 1
total_bill = bill_as_float * percent
number_of_persons = input("How many people to split the bill? ")
bill_per_person = total_bill / int(number_of_persons)
final_pay = round(bill_per_person, 2)
final_pay = "{:.2f}".format(bill_per_person)
#to round to 2 decimal places
#convert float into string
message = f"Each person should pay: {final_pay}"
print(message)
