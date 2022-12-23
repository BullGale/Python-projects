import requests
from datetime import datetime
import os

GENDER = "Male"
WEIGHT_KG = "60"
HEIGHT_CM = "170.68"
AGE = 18

APP_ID = os.environ["b357050f"]
API_KEY = os.environ["84becb4117msh1cb65b7f7c02178p101e20jsna3742e82e815"]

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = os.environ["https://v2-api.sheety.co/2bd39669b6917e21f0a8ba874254a384/workoutTracking/workouts"]

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

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    #No Auth
    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)


    #Basic Auth
    sheet_response = requests.post(
        sheet_endpoint, 
        json=sheet_inputs, 
        auth=(
            os.environ["USERNAME"], 
            os.environ["PASSWORD"],
        )
    )

    #Bearer Token
    bearer_headers = {
    "Authorization": f"Bearer {os.environ['TOKEN']}"
    }
    sheet_response = requests.post(
        sheet_endpoint, 
        json=sheet_inputs, 
        headers=bearer_headers
    )

    print(sheet_response.text)
