import requests  # Importerar requests-biblioteket för att kunna göra HTTP-anrop till API:et

class WeatherAPI:
    def __init__(self, api_key):
        self.api_key = api_key  # Sparar API-nyckeln som används för att autentisera med OpenWeatherMap

    def get_weather(self, city):  #  Hämtar väderdata från OpenWeatherMap API för en given stad.
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()  # Returnerar JSON-data
        else:
            return None  # Om något gick fel
