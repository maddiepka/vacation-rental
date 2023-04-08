# vacation-rental
**AirBnB-scrapper** - application gets from the user info about his future vacation stay,
validates it, and searches the AirBnB database to find vacation rentals.
Then the results are collected in an Airtable table so users can pick the best choice for them.

**Opis projektu:**
Program mający za zadanie uzyskanie od użytkownika informacji nt. przyszłego wyjazdu oraz warunków 
jakie musi spełniać jego wymarzone lokum. Po uzyskaniu danych wejściowych, waliduje ich poprawność 
(dobry format, czy daty są z przyszłości, czy przedział dat jest prawidłowy). 
Następnie przeszukuje bazę AirBnB i po uzyskaniu rekordów uzupełnia nimi formularze na AirTable. 
W odpowiedzi przesyła użytkownikowi link do tabeli w AirTable z uzyskanymi noclegami. 

**Technologie:**
Python,
BeautifulSoap,
Selenium


**Rozwiązania:**
- zadanie użytkownikowi pytań w celu uzyskania danych wejściowych, po wprowadzeniu odpowiedzi jej walidacja
- uzyskanie adresu URL wyszukiwania na AirBnB i za pomocą BeautifulSoap pobranie informacji dt. noclegu
- wpisanie uzyskanych rekordów do wcześniej przygotowanego formularza za pomocą Selenium
- wyświetlenie użytkownikowi linka z tabelą z wynikami jego wyszukiwania

**Screeny:**

- Prawidłowe wyszukiwanie użytkownika:
![correct input screenshot](./screenshots/user_input_correct.jpg)
- Wypełnianie formularza przez Selenium
![form screenshot](./screenshots/results_form.jpg)
- Wysłanie formularza, przejście przez Selenium do kolejnego rekordu
![form done screenshot](./screenshots/results_form_done.jpg)
- Wyświetlenie odpowiedzi użytkownikowi
![user results screenshot](./screenshots/user_results.jpg)
- Tabela z wynikami
![user table screenshot](./screenshots/table_results.jpg)

- Nieprawidłowe wyszukiwanie użytkownika (informacje są zadawane, aż użytkownik udzieli dobrej odpowiedzi)
![incorrect input screenshot](./screenshots/user_input_incorrect.jpg)
![incorrect 2 input screenshot](./screenshots/user_input_incorrect_2.jpg)


**Instalacja:**
Zgodnie z requirements.txt,
Uzupełnienie .env do swojej ścieżki chromedriver.exe


**Uruchomienie:**
python main.py

