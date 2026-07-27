import requests

# Replace with your OpenWeather API key
API_KEY = "YOUR_OPENWEATHER_API_KEY"

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    """
    Returns weather information.

    Example:
    {
        "temperature":30,
        "humidity":70,
        "condition":"Clouds",
        "wind":3.2
    }
    """

    if API_KEY == "YOUR_OPENWEATHER_API_KEY":

        # Demo mode

        return {
            "temperature": 30,
            "humidity": 72,
            "condition": "Partly Cloudy",
            "wind": 2.8
        }

    try:

        params = {
            "q": city,
            "appid": API_KEY,
            "units": "metric"
        }

        response = requests.get(
            BASE_URL,
            params=params,
            timeout=10
        )

        data = response.json()

        return {

            "temperature": data["main"]["temp"],

            "humidity": data["main"]["humidity"],

            "condition": data["weather"][0]["main"],

            "wind": data["wind"]["speed"]

        }

    except Exception:

        return {

            "temperature": "--",

            "humidity": "--",

            "condition": "Unavailable",

            "wind": "--"

        }
