import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "2b3eef62103e95200965a5dd20401fe0"
account_sid = "ACc5a7f305d6ce7b8d2fa66b590828ba73"
auth_token = "b3ddba2253721841abd85eb7bde300c1"

parameters = {
    "lat": 56.501041,      # 23.179190,
    "lon": 84.992455,      # 75.784248,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=parameters)
response.raise_for_status()
# print(response.status_code)   # 200
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔",
        from_="+12028580362",
        to="+919669915010"
    )
    print(message.status)

