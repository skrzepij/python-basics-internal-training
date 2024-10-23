## SLOWNIKI (DICTIONARY) - klucz:wartosc
# slownik = {klucz:wartosc, klucz:wartosc, klucz:wartosc}
wojewodztwa = { "MA": "azowieckie", "SL": "slaskie", "MP": "malopolskie", "DS": "dolnoslaskie" }
wojewodztwa["KP"] = "kujawsko-pomorskie" # dodanie nowego elementu
wojewodztwa["MA"] = "mazowieckie" # nadpisanie wartosci

print(wojewodztwa["MA"])

## KROTKI (TUPLE) - niezmienne
krotka = (1, 2, 4, "ABB", 2.4)
print(krotka[2])
# krotka[2] = 5 # nie zadziala

## OPERACJE NA LISTACH
lista = [20, 3, 4, 3, 60]
lista.append(22) # dodanie elementu na koniec
lista.insert(2, 33) # dodanie elementu na danej pozycji (pozycja, element)
lista.remove(3) # usuniecie elementu o danej wartosci
lista.sort() # sortowanie - tylko dla listy z elementami tego samego typu

# lista_2 = lista # lista_2 to referencja do listy
# lista_2[1] = 1000 # zmiana wartosci w obu listach - lista_2 to referencja do listy
lista_2 = lista.copy() # kopiowanie listy - zmiana wartosci w jednej nie zmienia wartosci w drugiej
# lista_2 = list(lista) # to samo co wyzej
lista_2[1] = 1000
print(lista)

lista_3 = [1, 2, 3]
lista.append(lista_3) # dodanie listy jako elementu
lista.extend(lista_3) # dodanie elementow z listy jako elementow
print(lista)

print(lista[6][1]) # drugi element szostego elementu listy (czyli drugi element listy_3)

## OPERACJE NA ZBIORACH
zbior = {1000, 2000, 3000}
zbior2 = {3, 4, 5, "ABC"}
zbior2.add(6) # dodanie elementu
zbior2.remove(4) # usuniecie elementu
print(zbior2)
zbior.update(zbior2) # dodanie elementow z jednego zbioru do drugiego
print(zbior)

## OPERACJE NA SLOWNIKACH
del wojewodztwa["KP"] # usuniecie elementu
print(wojewodztwa.keys()) # klucze
# print(wojewodztwa["LU"]) # KeyError
print(wojewodztwa.get("LU", "Brak wpisu")) # None - nie ma takiego klucza. Drugi argument to wartosc domyslna

## FUNKCJE
def dodaj(a, b):
    print("Suma liczb", a, "i", b, "to", a+b) # funkcja bez return
    # return a + b

dodaj(2, 3)
# print(dodaj(2, 3)) # None - funkcja nie ma return
dodaj("ABC", "DEF")
dodaj([1, 2, 3, 4], [5, 6])

def oblicz_podwyzke(podstawa, procent):
    return podstawa * (1 + procent / 100)
    # return podstawa * (procent / 100)

def oblicz_podatek(podstawa, procent = 0.18):
    return podstawa * procent

nowa_podstawa = oblicz_podwyzke(1000, 20)
podatek = oblicz_podatek(nowa_podstawa)
print(nowa_podstawa, podatek)