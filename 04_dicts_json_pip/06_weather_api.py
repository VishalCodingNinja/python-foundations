"""Current weather for a city from the OpenWeatherMap API.

Setup, inside your virtual environment (see README.md):
    pip install requests

Get a free API key at https://openweathermap.org, then set it:
    PowerShell:      $env:OPENWEATHER_API_KEY = "your-key"
    Windows cmd:     set OPENWEATHER_API_KEY=your-key
    macOS / Linux:   export OPENWEATHER_API_KEY=your-key
"""
import os
import sys

try:
    import requests
except ImportError:
    sys.exit("This demo needs requests. Run: pip install requests")

# Read the key from the environment, never hard-code a real key
API_KEY = os.environ.get("OPENWEATHER_API_KEY")
if not API_KEY:
    sys.exit("Set the OPENWEATHER_API_KEY environment variable first.")

BASE = "https://api.openweathermap.org"
url = BASE + "/data/2.5/weather"

city = input("City: ")
params = {"q": city, "appid": API_KEY,
          "units": "metric"}

response = requests.get(url, params=params, timeout=10)
if response.status_code != 200:
    sys.exit(f"Request failed ({response.status_code}): {response.text}")

data = response.json()  # JSON -> dict
print(data["name"], data["main"]["temp"], "°C")
print(data["weather"][0]["description"])
