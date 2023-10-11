import requests
from twilio.rest import Client
import os

some_env_var = os.environ.get("some var")

OWM_Endpoint = "https://api.openweathermap.org/data/3.0/onecall"
account_sid = "some sid"
auth_token = "some token"
api_key = "34033912bb7dd88d52ebb315ef6bb06f"
LON = 83.7636
LAT = 53.3606
EXCL = "current,minutely,daily,alerts"
parametr = {
    "lon": LON,
    "lat": LAT,
    "exclude": EXCL,
    "appid": api_key,

}

response = requests.get(
    url=OWM_Endpoint,
    params=parametr)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(body="umbrella", from_="somenumber", to="somenumber")
