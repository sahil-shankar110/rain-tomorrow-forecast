import requests
from dotenv import load_dotenv
import os
load_dotenv()
BASE_URL = "https://api.openweathermap.org/data/2.5/"
API_KEY = os.getenv("OPENWEATHER_API_KEY")

def degrees_to_compass(degrees):
    dirs = ['N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE',
            'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW']
    return dirs[int((degrees + 22.5) % 360 / 22.5)]

def get_current_weather(city):
    if not city or len(city) < 2:
        return None

    url = f"{BASE_URL}weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url, timeout=10)

    if response.status_code != 200:
        return None

    data = response.json()
    wind_dir = degrees_to_compass(data['wind'].get('deg', 0))

    return {
        'MinTemp': data['main']['temp_min'],
        'MaxTemp': data['main']['temp_max'],
        'WindGustDir': wind_dir,
        'WindGustSpeed': data['wind']['speed'] * 3.6,
        'Humidity': data['main']['humidity'],
        'Pressure': data['main']['pressure'],
        'Temp': data['main']['temp'],
        'City': data['name']
    }
