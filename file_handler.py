import json  # Inbyggt bibliotek för att hantera JSON-data

class FileHandler:
    def save_to_file(self, city, data):
        # Spara väderdata till en JSON-fil
        filename = f"{city}_weather.json"
        with open(filename, "w") as file:
            json.dump(data, file)  # Sparar data som JSON
        print(f"Väderdata sparad i filen {filename}.")
