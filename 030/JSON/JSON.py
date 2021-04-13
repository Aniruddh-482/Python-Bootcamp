# JSON: JavaScript Object Notation

#   To write in JSON:
#   json.dump()

#   To read in JSON:
#   json.load()

#   To update in JSON:
#   json.update()

# For Example: 
website = input("Website: ")
email = ("Email/Username: ")
password = ("Password: ")
new_data = {
    website: {
        "email": email,
        "password": password
    }
}

# # Writing in JSON
# with open("data.json", "w") as data_file:
#     json.dump(new_data, data_file, indent=4)  # Convert dictionary to json data.
 
# # Reading in JSON
# with open("data.json", "r") as data_file:
#     data = json.load(data_file)  # convert json data to python dictionary.
#     print(data)

# # Upadating JSON file
# with open("data.json", "r") as data_file:  
#     data = json.load(data_file)
#     data.update(new_data)
#     json.dump(data, data_file, indent=4)

# Final Code:
with open("data.json", "r") as data_file:
    # Reading old data
    data = json.load(data_file)
    # Updating old data with new data
    data.update(new_data)
with open("data.json", "w") as data_file:
    # Saving updated data
    json.dump(data, data_file, indent=4)

