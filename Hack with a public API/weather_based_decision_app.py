import requests # type: ignore
from dotenv import load_dotenv
import os 

load_dotenv()

API_KEY = os.getenv("API_KEY")

def connection(api_key, city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    return response

def get_weather_data(city):
    response = connection(API_KEY, city)

    if response.status_code != 200:
        print("Error:", response.text)
        return None

    data = response.json()

    return {
        "temp": data["main"]["temp"],
        "weather": data["weather"][0]["main"],
        "humidity": data["main"]["humidity"],
        "wind_speed": data["wind"]["speed"],
    }

def advice(weather_data):
    if weather_data is None:
        return

    print("\nAdvice:")

    if weather_data["temp"] > 35:
        print("🥵 It's very hot! Stay hydrated.")

    elif weather_data["temp"] < 15:
        print("🥶 It's cold! Wear a jacket.")

    if weather_data["weather"].lower() == "rain":
        print("☔ Carry an umbrella.")

    if weather_data["humidity"] > 80:
        print("💧 It's very humid today.")

if __name__ == "__main__":
    city = input("Enter city (default London): ") or "London"

    weather_data = get_weather_data(city)

    if weather_data:
        print("\nWeather Data:", weather_data)
        advice(weather_data)