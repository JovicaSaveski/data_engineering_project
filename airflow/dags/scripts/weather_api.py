import requests
import pandas as pd
from datetime import datetime

def get_weather_data(api_key, lat=41.961652, lon=21.621355):  #  coordinates for SKP Airport
    """
    Fetches weather data from OpenWeatherMap API for SKP Airport location
    
    Args:
        api_key (str): OpenWeatherMap API key
        lat (float): Latitude of location
        lon (float): Longitude of location
        
    Returns:
        pd.DataFrame: Weather data including temperature, precipitation, and wind speed
    """
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
        
        response = requests.get(url)
        response.raise_for_status()  
        
        data = response.json()
        
        weather_data = {
            'timestamp': datetime.now(),
            'temperature': data['main']['temp'],
            'precipitation': data.get('rain', {}).get('1h', 0),  # Rain in last hour, 0 if no rain
            'wind_speed': data['wind']['speed'],
            'weather_condition': data['weather'][0]['main']
        }
        
        return pd.DataFrame([weather_data])
        
    except requests.RequestException as e:
        print(f"Error fetching weather data: {str(e)}")
        return pd.DataFrame()
    except KeyError as e:
        print(f"Error parsing weather data: {str(e)}")
        return pd.DataFrame()