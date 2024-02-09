import requests

# User Input
user_input = input("Enter the name of a city or a zip code: ")

# OpenWeatherMap API Key and Base URL
api_key = "c40a9f55e06c083493b32985e488dabf"
base_url = "http://api.openweathermap.org/data/2.5/weather"

# API Request
params = {
    'q': user_input,
    'appid': api_key
}

response = requests.get(base_url, params=params)

# Check API Response
if response.status_code == 200:
    # Parse JSON Data
    try:
        weather_data = response.json()

        # Extract Relevant Information
        temperature = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']
        description = weather_data['weather'][0]['description']

        # Display Weather Information
        print(f"Weather in {user_input}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
        print(f"Description: {description}")
    except KeyError as e:
        print(f"Error parsing weather data. Missing key: {e}")
    except Exception as e:
        print(f"Error retrieving weather data. Exception: {e}")
