import requests
import os

API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

print("================================")
print("       WEATHER APP")
print("================================")
def get_weather(city):

    if not API_KEY:
        print("API key not found!")
        return

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        response.raise_for_status()

        data = response.json()

        print("\n--- WEATHER DETAILS ---")
        print("City:", data["name"])
        print("Temperature:", data["main"]["temp"], "°C")
        print("Weather:", data["weather"][0]["description"])
        print("Humidity:", data["main"]["humidity"], "%")
        print("Wind Speed:", data["wind"]["speed"], "m/s")

    except requests.exceptions.HTTPError:
        print("City not found or API request failed!")

    except requests.exceptions.RequestException:
        print("Network connection error!")

    # Main Program
city = input("\nEnter city name: ")

get_weather(city)