## FUNKCJE - Zadania
def mniejsza(x, y):
    if x < y:
        return x
    else:
        return y

    # return x if x < y else y # to samo co powyzej - zapis skrocony

    x = 10
    y = 15
    print(mniejsza(x, y))

def najwieksza(lista):
    maks = lista[0]
    for x in lista:
        if x > maks:
            maks = x
    return maks

def najwiekszaSort(lista):
    lista.sort()
    return lista[-1]

def najwiekszaRange(lista):
    maks = lista[0]
    for i in range(len(lista)):
        if lista[i] > maks:
            maks = lista[i]
    return maks

def najwiekszaMax(lista):
    return max(lista)

lista = [4, 70, 4, 12, 4]
print(najwiekszaMax(lista))

# WBUDOWANE FUNKCJE NA LISTACH
print(
    "Dlugosc",  len(lista),
    "Najmniejszy", min(lista),
    "Najwiekszy",  max(lista),
    "Suma",  sum(lista)
)

## ZBIORY - Petla for
zbior = {3, 4, 5, 5, 5, 3, 13, 14}
for i in zbior:
    print(i)

## SLOWNIKI - Petla for
slownik = { 1: "jeden", "dwa": 1, 12.3: 345.7 }
for klucz in slownik:
    print(klucz, slownik[klucz]) # klucz, wartosc

## STRINGI - konkatenacja
s1 = "Abc"
s2 = "def"
wynik = s1 + s2
tekst = "To jest przykładowy tekst"
wynik = tekst[:5] # Rezultat: "To je" - od poczatku do 5 znaku
wynik = tekst[::-1] # Rezult: "kset ywodlawykjirzT" - odwrocony tekst
print(wynik)

## STRINGI - metody
dane = "Adam;Ewa;Celina;Dariusz"
lista_osob = dane.split(";") # podzial tekstu na liste
print(lista_osob)

for i in lista_osob:
    print("Witaj", i)

tekstOsob = ";".join(lista_osob) # laczenie listy w tekst - odwrotnosc split

## STRINGI - Escape characters
tekstZCudzyslowem = "To jest \"przykładowy\" tekst" # To jest "przykładowy" tekst
tekstZUkosnikiem = "C:\\Windows\\System32" # C:\Windows\System32
tekstZEnterem = "To jest tekst\nz enterem \t" # To jest tekst (enter) z enterem (tabulator)

## STRINGI - formatowanie
imie = "Adam"
nazwisko = "Kowalski"
print(f"Witaj " + imie) # konkatenacja
print(f"Witaj {imie}") # f-string - od Python 3.6

stringZeZmienna = "Witaj {} {}".format(imie, nazwisko) # formatowanie
stringZeZmiennaIKolejnoscia = "Witaj {1} {0}".format(imie, nazwisko) # formatowanie
stringZAliasami =  "Witaj {na} {im}".format(im=imie, na=nazwisko) # formatowanie
print(stringZAliasami)