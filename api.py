import requests

class Weather:

    def __init__(self):
        self.city = ""
        self.api_key = '9b42fcb26e694c1e971105725230404'
        self.temperature = ""
        self.description = ""

    def weather_api(self):
        self.city = input('Please select a city: ').capitalize()
        url = f'http://api.weatherapi.com/v1/current.json?key={self.api_key}&q={self.city}&aqi=no'

        response = requests.get(url)
        weather_data = response.json()

        self.temperature = weather_data['current']['temp_c']
        self.description = weather_data['current']['condition']['text']