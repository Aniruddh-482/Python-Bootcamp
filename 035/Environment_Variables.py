# Understanding Environment Variables and Hiding API Keys

# Environment Variables #
# --------------------- #

# We use Environment Variables to store important data when we are uploading our data on internet, so that no one else can see them.

# (In Console)
# ~ $ env

# ~ $ export OWM_API_KEY=demo_api_key   # (API_Key)
# ~ $ env
# # Environment Variable OWM_API_KEY is saved.

# ~ $ export AUTH_TOKEN=demo_auth_token   # (AUTH_TOKEN)
# ~ $ env
# Environment Variable AUTH_TOKEN is saved.

# Updated Code:

import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = os.environ.get("OWM_API_KEY")
account_sid = "demo_account_sid"
auth_token = os.environ.get("AUTH_TOKEN")

parameters = {
    "lat": 23.179190,
    "lon": 75.784248,
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
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔",
        from_="+12028580362",
        to="+919669915010"
    )
    print(message.status)

