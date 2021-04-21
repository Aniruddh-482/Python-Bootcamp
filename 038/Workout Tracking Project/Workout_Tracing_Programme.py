import requests

GENDER = "male"
WEIGHT_KG = 55
HEIGHT_CM = 174
AGE = 18

APP_ID = "c6745e5f"
API_KEY = "931c0bf1735a52e113e9a227ff635ad9"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)

