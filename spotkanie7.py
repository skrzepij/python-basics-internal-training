## BAZA DANYCH - operacje

dane = [
    {"imie": "Adam", "drugie": "Janusz", "nazwisko": "Kowalski", "wiek": 30},
    {"imie": "Ewa", "drugie": "Eliza", "nazwisko": "Ebacka", "wiek": 24},
    {"imie": "Dariusz", "drugie": "Dionizy", "nazwisko": "Dabacki", "wiek": 30},
   # {12: 233,}, # to nie zadziala dla bazy danych, ale zadziala dla JSON
   # {22: None}, # to nie zadziala dla bazy danych, ale zadziala dla JSON - None to null
]
import sqlite3

polaczenie = sqlite3.connect("dane.sqlite") # polaczenie z baza danych (plik) - utworzenie bazy danych w pliku dane.sqlite (jesli nie istnieje)
kursor = polaczenie.cursor()

# utworzenie tabeli osoba
sql_string = """
CREATE TABLE IF NOT EXISTS osoba (
    imie varchar(255) Not Null,
    drugie varchar(255) Not Null,
    nazwisko varchar(255) Not Null,
    wiek int Null
);
"""

# dodanie wiersza do tabeli
sql_string = 'insert into osoba (imie, drugie, nazwisko, wiek) values ("Beata", "Marta", "babacka", 17)'
kursor.execute(sql_string)
polaczenie.commit() # zatwierdzenie zmian w bazie danych

# dodanie wierszy do tabeli - wersja z parametrami (bezpieczniejsza) - zabezpieczenie przed SQL Injection
sql_string = 'insert into osoba (imie, drugie, nazwisko, wiek) values (?, ?, ?, ?)'
for wiersz in dane:
    kursor.execute(sql_string, (wiersz["imie"], wiersz["drugie"], wiersz["nazwisko"], wiersz["wiek"]))
    polaczenie.commit() # zatwierdzenie zmian w bazie danych

# odczytanie wierszy z tabeli
sql_string = "SELECT * FROM osoba"
kursor.execute(sql_string)

wiersze = kursor.fetchall()
for wiersz in wiersze:
    print(wiersz)

kursor.close()
polaczenie.close()

## JSON
import json

## JSON - zapisywanie
with open("dane.json", "wt", encoding = "utf-8") as plik_json:
    json.dump(dane, plik_json, indent = 4) # zapisanie do pliku - dane w formacie JSON - indent - wciecia
# json.dumps() # zapisanie do stringa

## JSON - odczytywanie
with open("dane.json", "rt", encoding = "utf-8") as plik_json:
    dane_json = json.load(plik_json) # odczytanie z pliku - dane w formacie JSON
print(dane_json)

import pickle # zapisywanie obiektow Pythona - niezalecane do zapisywania danych do plikow
with open("plik_json","wb") as plik_json:
    pickle.dump(dane, plik_json) # zapisanie do pliku - dane w formacie Pythona
with open("plik_json","rb") as plik_json:
    dane_pickle = pickle.load(plik_json) # odczytanie z pliku - dane w formacie Pythona