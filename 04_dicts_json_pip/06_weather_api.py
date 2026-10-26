"""Module 4 · Demo: use the OpenWeatherMap API

Asks for a city, requests its current weather from the OpenWeatherMap web
API and prints the temperature and conditions.

Setup, inside your virtual environment (see README.md):
    pip install requests

Get a free API key at https://openweathermap.org, then set it:
    PowerShell:      $env:OPENWEATHER_API_KEY = "your-key"
    Windows cmd:     set OPENWEATHER_API_KEY=your-key
    macOS / Linux:   export OPENWEATHER_API_KEY=your-key

Run it:  python 04_dicts_json_pip/06_weather_api.py
"""
import os
import sys

# requests isn't part of Python; it's installed with pip.
# If it's missing, stop with a helpful message instead of a crash.
try:
    import requests
except ImportError:
    sys.exit("This demo needs requests. Run: pip install requests")

# Read the key from the environment, never hard-code a real key:
# code gets shared, and a key written in the code gets shared with it
API_KEY = os.environ.get("OPENWEATHER_API_KEY")
if not API_KEY:
    sys.exit("Set the OPENWEATHER_API_KEY environment variable first.")

# The web address of the "current weather" service
BASE = "https://api.openweathermap.org"
url = BASE + "/data/2.5/weather"

city = input("City: ")
# Query parameters: q is the city, appid your key, metric means Celsius
params = {"q": city, "appid": API_KEY,
          "units": "metric"}

# Send the request; timeout stops it waiting forever if the server is slow
response = requests.get(url, params=params, timeout=10)
# Status 200 means OK; anything else (401 bad key, 404 unknown city) failed
if response.status_code != 200:
    sys.exit(f"Request failed ({response.status_code}): {response.text}")

data = response.json()  # JSON -> dict
# The answer is nested JSON, so read it step by step
print(data["name"], data["main"]["temp"], "°C")
print(data["weather"][0]["description"])
