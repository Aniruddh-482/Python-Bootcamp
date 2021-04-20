# Dictionary in List #
# ------------------ #

# You are going to write a program that adds to a travel_log. You can see a travel_log which is a List that contains 2 Dictionaries.
# Write a function that will work with the following line of code on line 21 to add the entry for Russia to the travel_log.

# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])

# You've visited Russia 2 times.
# You've been to Moscow and Saint Petersburg.

# DO NOT modify the travel_log directly. You need to create a function that modifies it.

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

# TODO: Write the function that will allow new countries
# to be added to the travel_log. 
def add_new_country(country, visits, cities):
    updated_travel_log = {
        "country": country,
        "visits": visits,
        "cities": cities,
    }
    travel_log.append(updated_travel_log)
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)

# or

# TODO: Write the function that will allow new countries
# to be added to the travel_log.
def add_new_country(name, visit_count, cities_visited):
  new_country = {}
  new_country["country"] = name
  new_country["visits"] = visit_count
  new_country["cities"] = cities_visited
  travel_log.append(new_country)
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
