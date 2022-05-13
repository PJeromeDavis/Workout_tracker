import requests
import datetime as dt
import os

SHEETY_URL = os.environ.get("SHEETY_URL")
USERNAME = os.environ.get("MY_USERNAME")
PASS = os.environ.get("PASS")
nutritionix_url = "https://trackapi.nutritionix.com/v2/natural/exercise"
APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")
nutritionix_headers = {"x-app-id": APP_ID, "x-app-key": API_KEY}
activity = input("What exercise did u do today?:")

request_parameters = {"query":activity}

response = requests.post(url=nutritionix_url, json=request_parameters, headers=nutritionix_headers)
exercise = response.json()["exercises"][0]["user_input"]
exercise_time = response.json()["exercises"][0]["duration_min"]
calories_burned = response.json()["exercises"][0]["nf_calories"]
print(f"You {exercise} for {exercise_time}mins and burned {calories_burned} calories.")
year = dt.datetime.now().year
month = dt.datetime.now().month
day = dt.datetime.now().day
today = f"{year}/{month}/{day}"
current_time = dt.datetime.now()
parameters = {"workout":{"date":today,
                         "time":current_time.strftime("%H"),
                         "exercise":exercise,
                         "duration":exercise_time,
                         "calories":calories_burned}}
sheety_response = requests.post(url=SHEETY_URL, json=parameters, auth=(USERNAME, PASS))
print(os.environ.get("SHEETY_URL"))
#return_response = requests.get(url="https://api.sheety.co/d34b587bde75a73f2274d0add3c42b6d/myWorkouts/workouts", auth=(USERNAME, PASS))
#print(return_response.json())