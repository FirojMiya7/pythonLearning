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
    apiKey = "f66db77dbdf448fc3b401eafc5154bab"  # OpenWeatherMap api key, you can get it for free by signing up on their website
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKey}&units=metric"

    try:
        response = requests.get(url)
        print("Status Code:", response.status_code)   # debug line
        
        data = response.json()
        print("Full Response:", data)   # debug line

        if response.status_code != 200:
            print("Error:", data.get("message"))
            return

        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]

        print(f"\nWeather in {city.title()}:")
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%")

    except requests.exceptions.RequestException as e:
        print("Request Error:", e)


if __name__ == "__main__":
    print("===== Weather App =====")
    city = input("Enter city name: ")
    fetchWeather(city)
