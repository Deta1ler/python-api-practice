import json
import sys
import requests


if len(sys.argv) != 3:
    sys.exit


response = requests.get("https://api.open-meteo.com/v1/forecast?latitude=" + sys.argv[1] + "&longitude=" + sys.argv[2] + "&current_weather=true")

json_response = response.json()

temperature = json_response["current_weather"]["temperature"]
time = json_response["current_weather"]["time"]

print(f"Time2: {time}; Temperature1: {temperature}")
