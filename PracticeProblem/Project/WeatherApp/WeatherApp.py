# Project 5: Weather App (API – Beginner)
"""
Requirements:
City name input
Weather data fetch (API)

Show:
temperature
humidity

Use:
requests module
functions

Goal: API concept introduction
"""
import requests

def fetchWeather(city):
    api_key = "f4eecc61fa25a17ed62ea79b432b44ca"    # OpenWeatherMap API key, where you can sign up for a free key at https://openweathermap.org/api

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code != 200:
            print("Error:", data.get("message", "City not found"))
            return

        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]

        print(f"\nWeather in {city.title()}:")
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%")

    except requests.exceptions.RequestException:
        print("Network error. Please check your internet connection.")


if __name__ == "__main__":
    print("===== Weather App =====")
    city = input("Enter city name: ")
    fetchWeather(city)
