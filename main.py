from weather_app import WeatherApp
from file_handler import FileHandler

def main():
    api_key = "6e600812e2c89be5083d75036f5dbdd3" # API nyckeln från OpenWeatherMap.com
    app = WeatherApp(api_key)
    file_handler = FileHandler()

    city = input("Ange stad: ")  # Enkel input från användaren
    data = app.api.get_weather(city)  # Hämta väderdata

    if data:
        app.show_weather(city)  # Visa väder
        # Fråga användaren om dem vill spara väderdata
        save = input("Vill du spara väderdata? (ja/nej): ").lower()
        if save == "ja":
            file_handler.save_to_file(city, data)  # Spara till fil
    else:
        print("Inget väder hittades för den staden.")

if __name__ == "__main__":
    main()  # Kör huvudprogrammet
