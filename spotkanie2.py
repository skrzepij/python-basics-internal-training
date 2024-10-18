## ZMIENNE
x = 1 # int
y = 1.1 # float / calkowita
test = "to jest tekst przykladowy" # string

print(x)
x = "abc"
print(x)

## OPERACJE NA ZMIENNYCH
x = 10
print(x * y)
print(13 % 5) # reszta z dzielenia (modulo)
print( 2 ** 3) # potegowanie
print(10 // y) # dzielenie calkowite

x = x + 2 # x += 2
print(x)

## INSTRUKCJE WARUNKOWE
if 3 != 3:
    print("rozne")

##  PETLA WHILE

# suma liczb od 1 do 10
a = 1
suma = 0
while a <= 10:
    print(a)
    suma += a
    a += 1

print("suma", suma)

# suma kwadratow liczb parzystych od 1 do 10
b = 2
sumaKwadratow = 0
while b <= 10:
    sumaKwadratow += b*b
    b += 2

print("suma kwadratow", sumaKwadratow)

## PETLA FOR
sumaFor = 0
for i in range(2, 11, 2): # pierwszy argument to poczatek, drugi to koniec (nie wliczajac), trzeci to krok
    sumaFor += i*i
    print(i)
print("suma for", sumaFor)

for i in range(21, 6, -3):
    print(i)

## LISTY
lista = [3, 4, 5, 4.5, 6.8, "ABC", 1,  "abc"]
print(lista)
print(lista[0])

lista_2 = lista[1:4] # wyciaganie podlisty - od 1 do 4 (bez 4)
print(lista_2)
lista_3 = lista[3:-1] # od 3 do przedostatniego
lista_4 = lista[3:] # od 3 do konca
lista_5 = lista[::2] ## co drugi element listy - trzeci argument to krok\
lista_6 = lista[::-1] ## odwrocenie listy

## ZBIORY (SET)
zbior = {3, 4, 5, 4.5, "abc", 4, 5}
print(zbior)
if 3 in zbior:
    print("jest 3")
if 88 not in zbior:
    print("nie ma 88")
if {3, "abc", 5} < zbior: # sprawdzenie czy zbiór jest podzbiorem zbioru
    print("jest podzbiorem")