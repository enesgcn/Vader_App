from weather_api import WeatherAPI # Importerar klassen WeatherAPI för att kunna hämta väderdata

class WeatherApp:
    def __init__(self, api_key):
        self.api = WeatherAPI(api_key)

    def show_weather(self, city):
        data = self.api.get_weather(city)  # Hämtar väderdata
        if data:
            # Visar grundläggande väderinformation
            temp = data['main']['temp']
            description = data['weather'][0]['description']
            print(f"Vädret i {city}: {temp}°C, {description}")
        else:
            print("Kunde inte hämta väderdata.")
