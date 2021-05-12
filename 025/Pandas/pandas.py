with open("weather_data.csv") as data_file:
    data = data_file.readlines()
    print(data)
# OR
import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    # print(data)
    temperature = []
    for row in data:
        # print(row)
        if row[1] != "temp":
            temperature.append(int(row[1]))
    print(temperature)
# OR
import pandas

data = pandas.read_csv("weather_data.csv")
print(data)
print(data["temp"])
print(type(data))  # DataFrame (Two dimensional)
print(type(data["temp"]))  # Series (One dimensional)

# To convert into Dictionary
data_dict = data.to_dict()
print(data_dict)

# To convert into List
temp_list = data["temp"].to_list()
print(len(temp_list))

# For average of temperature
# average = sum(temp_list) / len(temp_list)
# print(average)
# or
print(data["temp"].mean())

# To get the maximum value
print(data["temp"].max())

# Get Data in Columns
# print(data["condition"])
# or
print(data.condition)

# Get Data in Rows
print(data[data.day == "Monday"])

# Get data in rows of highest temperature
print(data[data.temp == data.temp.max()])

# Get condition of row = Monday
monday = data[data.day == "Monday"]
print(monday.condition)

# Convert Monday's temperature to Fahrenheit
monday_temp = int(monday.temp)
monday_temp_F = monday_temp * 9/5 + 32
print(monday_temp_F)

# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 43]
}
data = pandas.DataFrame(data_dict)
# print(data)
data.to_csv("new_data.csv")  # Create a new csv file
