osoby = ["Adam", "Ewa", "Celina"]

## STRINGI - OPERACJE NA STRINGACH
for osoba in osoby:
    print(f"Witaj {osoba}")

someNumber = 10
print(f"Mam {someNumber + 17}")
print(r"Tekst z \n nowa linia") # r - raw string - traktuj tekst doslownie

txt = "I like bananas"
replaced = txt.replace("bananas", "apples")
print(replaced)

## LISTY - OPERACJE NA LISTACH
list1 = [1, 5, 3, 10]
# wylicz kwadraty
list2 = []
for i in list1:
    # tylko dla list nieparzystych
    if i % 2 == 1:
        list2.append(i*i)

# Zapis skrocony
list2 = [i * i for i in list1 if i % 2 == 1]
print(list2)

x = 13
if x % 2 == 1:
    print("nieparzysta")
else:
    print("parzysta")

# inline if
s = "nieparzysta" if x % 2 == 1 else "parzysta"

## ZBIORY - OPERACJE NA ZBIORACH
list3 = 1, 5, 3, 10, 3, 5
zbior1 = {x*x for x in list3}
print(zbior1) # {1, 9, 25, 100} - zbiory nie maja duplikatow

## RZUTOWANIE TYPÓW
jakasLiczba = 1
jakisTekst = "2"
print(jakasLiczba + int(jakisTekst)) # 3
print(str(jakasLiczba) + jakisTekst) # "12"

## TYP FLOAT
float1 = "1.1"
float2 = "2.2"
print(float(float1) + float(float2)) # 3.3000000000000003 - wynik jest nieco inny niz sie spodziewamy

lista4 = [1, 4, 2, 6, 5, 5, 5, 5]
zbior3 = set(lista4)
zbior4 = {2, 3, 4, 5}
lista5 = list(zbior4)

## OPERACJE NA PLIKACH
# Zapisanie do pliku
plik1 = open("test1.txt", "wt", encoding='utf-8') # tworzenie pliku do zapisu tekstowego (w - write, t - text) i kodowanie utf-8
plik1.write("To jest tekst do zapisania\n")
plik1.close()

# Odczytanie z pliku
plik2 = open("test1.txt", "rt", encoding='utf-8') # odczyt pliku tekstowego (r - read, t - text) i kodowanie utf-8
readText = plik2.read()
plik1.close()

print(readText)
# Zapisanie listy do pliku, oddzielona tabem
listaDoZapisu = ["aaaa", "bbb", "cccc"]
plik3 = open("lista.txt", "wt", encoding='utf-8')
# for i in listaDoZapisu:
    # plik3.write(i + "\t")
plik3.write("\t".join(listaDoZapisu))