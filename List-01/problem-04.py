import json
import time

import requests


def weather_data():
    api_url = "https://api.open-meteo.com/v1/forecast?latitude=24.37&longitude=88.60&hourly=temperature_2m,relativehumidity_2m,windspeed_10m"
    res = requests.get(api_url)
    content = res.content.decode("UTF-8")

    res_json = json.loads(content)
    print("Date: ", res_json["hourly"]["time"][0].split("T")[0])
    print("Temperature: ", res_json["hourly"]["temperature_2m"][0], "C")

    time.sleep(30 * 60)  # function wil execute after every 30 mins


while True:
    weather_data()
