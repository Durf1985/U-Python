import requests
import json
from datetime import datetime
import os

# APP_ID = os.environ["APP_ID"]
# API_KEY = os.environ["API_KEY"]

APP_ID = "05498243"
API_KEY = "4d0fa9d5e46e8064ba98410e0bb66d9b"
GENDER = "male"
WEIGHT = 71.5
HEIGHT = 165.0
AGE = 38
query = "Ran 2 miles and walked for 3Km."

endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

header = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,

}

param = {
    "query": query,
    # "query": input("Tell me which exercise you did: "),
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": 38
}

response = requests.post(url=endpoint, json=param, headers=header)

response.raise_for_status()
result = response.json()
print(json.dumps(result, indent=4))

sheety_endpoint = "https://api.sheety.co/8153e6a5fe4974db9df23214e6e642ce/myWorkouts/workouts"

today_date = datetime.now().strftime("%d%m%Y")
now_time = datetime.now().strftime("%X")
print(today_date, now_time)
# p{}
for exer in result["exercises"]:
    sheety = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exer["name"].title(),
            "duration": exer["duration_min"],
            "calories": exer["nf_calories"]
        }
    }

    # print(json.dumps(sheety, indent=4))
    sheety_response = requests.post(url=sheety_endpoint, json=sheety, auth=("", ""))
    print(sheety_response.text)
