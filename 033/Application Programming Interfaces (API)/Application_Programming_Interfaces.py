# Application Programming Interfaces (API)

# An Application Programming Interface (API) is a set of commands, functions, protocols, and objects
# that programmers can use to create software or interact with an external system.

import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
# print(response.status_code)
# if response.status_code != 200:
#     raise Exception("Bad response from ISS API")
response.raise_for_status()

longitude = response.json()["iss_position"]["longitude"]
latitude = response.json()["iss_position"]["latitude"]

iss_position = (longitude, latitude)

print(iss_position)
