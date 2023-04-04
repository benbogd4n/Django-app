from api import Weather

weather = Weather()
weather.weather_api()


print(f'The temperature in {weather.city} is {weather.temperature:.1f}°C and the weather is {weather.description}.')