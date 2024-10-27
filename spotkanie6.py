## PLIKI - operacje na plikach
plik_zapis = open("nazwa_pliku.txt", "wt", encoding='utf-8') # tworzenie pliku do zapisu tekstowego (w - write, t - text) i kodowanie utf-8
plik_odczyt = open("nazwa_pliku.txt", "rt", encoding='utf-8')  # odczyt pliku tekstowego (r - read, t - text) i kodowanie utf-8
plik_zapis.write("To jest tekst do zapisania\n")
plik_zapis.close()

plik_dodatek = open("nazwa_pliku.txt", "at", encoding='utf-8') # otwarcie pliku do dopisywania (a - append)
plik_dodatek.write("To jest kolejny tekst do zapisania\n")
plik_dodatek.close()

# plik_istnieje - próba utworzenia pliku, który już istnieje
# exclusive creation - plik zostanie utworzony tylko jeśli nie istnieje
###############################################
# plik_istnieje = open("nazwa_pliku.txt", "xt", encoding='utf-8') # tworzenie pliku do zapisu tekstowego (x - exclusive creation)
# plik_istnieje.write("To jest tekst do zapisania\n")
# plik_istnieje.close()

## Utworzenie pliku CSV
dane = [
    {"imie": "Adam", "drugie": "Janusz", "nazwisko": "Kowalski", "wiek": 30},
    {"imie": "Ewa", "drugie": "Eliza", "nazwisko": "Ebacka", "wiek": 24},
    {"imie": "Dariusz", "drugie": "Dionizy", "nazwisko": "Dabacki", "wiek": 30},
]
kolumny = ["imie", "drugie", "nazwisko", "wiek"]

plik_csv = open("dane.csv", "wt", encoding='utf-8')
plik_csv.write(";".join(kolumny) + "\n")

for wiersz in dane:
    print(wiersz)
    for kolumna in kolumny:
        plik_csv.write(str(wiersz[kolumna]) + ";")
    # plik_csv.write(";".join([str(wiersz[kolumna]) for kolumna in kolumny]) + ";") # zapisanie wiersza w jednej linii
    plik_csv.write("\n")
plik_csv.close()

## HTML - zapisanie tabeli
def przygotuj_wiersz_html (wiersz_a):
    # html = "<tr><td>"
    # html += "</td><td>".join([str(x) for x in wiersz_a])
    # html += "</td></tr>\n"
    return f"<tr><td>{'</td><td>'.join([str(x) for x in wiersz_a])}</td></tr>\n"
    # return "<tr>" + "".join(["<td>" + str(wiersz[kolumna]) + "</td>" for kolumna in kolumny]) + "</tr>"

plik_html = open("tabela.html", "wt", encoding='utf-8')
plik_html.write("<html><head></head><body><table border=\"1\">")
plik_html.write(przygotuj_wiersz_html(kolumny))

for wiersz in dane:
    plik_html.write(przygotuj_wiersz_html([str(wiersz[x]) for x in wiersz]))
# plik_html.write("<tr>")
# for kolumna in kolumny:
#     plik_html.write("<th>" + kolumna + "</th>")
# plik_html.write("</tr>")
plik_html.write("</table></body></html>")
plik_html.close()

## BAZY DANYCH
import sqlite3
polaczenie = sqlite3.connect("dane.sqlite") # polaczenie z baza danych (plik) - utworzenie bazy danych w pliku dane.sqlite (jesli nie istnieje)
kursor = polaczenie.cursor()

sql_string = """
CREATE TABLE IF NOT EXISTS osoba (
    imie varchar(255) Not Null,
    drugie varchar(255) Not Null,
    nazwisko varchar(255) Not Null,
    wiek int Null
);
"""
kursor.execute(sql_string)
polaczenie.commit()
kursor.close()
polaczenie.close()