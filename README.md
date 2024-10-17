Väderapplikation by Enes..

Beskrivning:
Denna Python-applikation hämtar aktuell väderinformation för en vald stad från OpenWeatherMap API och visar vädret för användaren. Programmet erbjuder också möjlighet att spara väderinformationen till en fil i JSON-format.

Funktioner:
    Hämtar väderdata från ett offentligt väder-API (OpenWeatherMap).
    Visar aktuell temperatur och väderbeskrivning för en stad som användaren anger.
    Möjlighet att spara väderinformationen till en fil i JSON-format.


För att kunna köra detta program behöver du:
    Python 3.6 eller senare
    requests-biblioteket (kan installeras med pip)

Installation
    Klona detta repo eller ladda ner filerna
    Du kan antingen ladda ner alla projektfiler eller klona detta projekt till din dator.
    Installera nödvändiga bibliotek
    Öppna terminalen eller kommandotolken för att installera requests-biblioteket:
    
   Hämta din API-nyckel från OpenWeatherMap:
       Gå till OpenWeatherMap och skapa ett konto.
        När du har ett konto, gå till ditt konto och skapa en ny API-nyckel.
        Kopiera din API-nyckel.

Användning:
    Lägg till din API-nyckel
    Öppna filen main.py i en textredigerare och ersätt följande rad med din faktiska API-nyckel:

api_key = "din_api_nyckel"

Exempel:

python

api_key = "1234567890abcdef"

Kör programmet
När du har lagt till din API-nyckel, du kan köra main.py filen

När programmet körs kommer det att be dig att ange en stad. Skriv in en stad som du vill hämta vädret för, till exempel:
  Ange stad: Stockholm

Se väderinformationen:
  Programmet kommer att hämta och visa temperaturen och väderbeskrivningen för den stad du angav, till exempel:
Vädret i Stockholm: 15°C, klart

Spara väderdata: 

  Programmet frågar dig om du vill spara väderinformationen i en fil. Svara med "ja" om du vill spara, eller "nej" om du inte vill. Om du väljer "ja", kommer en JSON-fil med väderinformationen att skapas och sparas i projektmappen.

Filstruktur:
  Följande filer ingår i projektet:

   weather_api.py: Hämtar väderdata från OpenWeatherMap API.
    weather_app.py: Visar väderdata för användaren.
    file_handler.py: Sparar väderdata till en fil.
    main.py: Huvudprogrammet som kör alla delar tillsammans.
    
