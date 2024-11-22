x = None
# Usuwanie z miejsca w pamieci
del x #  nie usuwa obiektu, tylko referencje do niego- zmienna x nie istnieje

# print(x) # NameError: name 'x' is not defined

x = "1"
y = "1"
print(x == y, x is y) # True True - x i y wskazuja na ten sam obiekt w pamieci
# roznica między x == y a x is y polega na tym, że x == y porównuje wartości obiektów, a x is y porównuje referencje do obiektów

lista1 = [1, 2, 3, 4]
lista2 = lista1
lista2[1] = 1000
print(lista1 == lista2, lista1 is lista2) # True True - x i y wskazuja na ten sam obiekt w pamieci
# nie dotyczy to typów prostych (int, float, str, bool) - wtedy x == y i x is y zwracają True - bo są to typy proste

## Typy
print(type("1.0")) # <class 'str'>
def dodaj(a: int, b: int) -> int:
    x1 = float(x) if type(x) == str else x
    y1 = float(y) if type(y) == str else y
    return x1 + y1

print(dodaj("1", 1)) # 2

# Typ bool
print(type(True)) # <class 'bool'>

# Operatory porównania - zwracają wartość typu bool
num1 = 4
num2 = 7
bool1 = num1 > 7
print(bool1) # False

if bool1:
    print("Prawda")

if -1: # True - każda liczba różna od 0 i kazdy string rozny od ""  jest traktowana jako True
    print("Prawda")
else:
    print("Falsz")

lista3 = [True, False, -1, 0, 10, 0.0, "", {}, [], [0], None, "abc"]
for i in lista3:
    if i:
        print(i, " - Prawda")
    else:
        print(i, " - Falsz")

# and or not  # operatory logiczne
if 1 < 2 and not(3 < 2):
    print("Prawda")

# MODUL DATETIME
import datetime

now = datetime.datetime.now()
print(now)
timeX = datetime.datetime(2022, 12, 31, 23, 59, 59) # rok, miesiac, dzien, godzina, minuta, sekunda
timeZ = timeX + datetime.timedelta(seconds = 10) # dodanie 10 sekund do daty
print(timeX, timeZ, timeZ > timeX) # 2022-12-31 23:59:59 2023-01-01 00:00:09 True

# Ile dni minelo od poczatku swiata
start = datetime.datetime(1, 1, 1) # rok, miesiac, dzien
now = datetime.datetime.now()
delta = now - start
print(delta.days)

## MODUL DECIMAL
from decimal import Decimal # importowanie klasy Decimal z modulu decimal - do obliczen finansowych - unika problemow z float
decimal1 = Decimal("1.1")
decimal2 = Decimal("2.2")
decimalX = decimal1 + decimal2
print(decimalX) # 3.3

## MODUL ATLASSIAN CONFLUENCE
from atlassian import Confluence
from modul.token import confluence_token

confluence = Confluence(url='https://intranet.coi.gov.pl/', token = confluence_token)

space_key = "~rskrzepij"
page_title = "Testowa strona"
page_id  = confluence.get_page_id(space_key, page_title)

zawartosc = confluence.get_page_by_id(page_id, expand='body.storage')
print(zawartosc["body"]["storage"]["value"])

confluence.update_page(page_id, page_title, "Nowa tresc strony", representation='storage') # representation='storage' - formatowanie tekstu