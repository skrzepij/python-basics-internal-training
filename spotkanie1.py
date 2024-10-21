import math

# Wyswietlenie tekstu na ekranie
#print("witaj świecie")
print(1234, 23, 'ala ma kota', sep=';\t') # okreslenie separatora (\t - tabulator)
print(2*15)


# Zmienne
# konwencja nazewnictwa 'snake_case'
x = 5
x = 6
print("mnozenie zmiennych", x*x)

a = 1
A = 2
print(a, A)

# instrukcje warunkowe
x = 10
y = 15

if x > y:
    print("wieksze")
elif x < y:
    print("mniejsze")
else:
    print("rowne")


# operacje na bibliotece math
print(math.sqrt(9))
# a*x^2 + b*x + c = 0

a = 1
b = 5
c = 6

delta = b*b - 4*a*c

if delta < 0:
    print("brak rozwiazan")
elif delta == 0:
    print("jedno rozwiazanie", -b/(2*a))
else:
    pierwiastek = math.sqrt(delta)
    x1 = (-b - pierwiastek) / (2*a)
    x2 = (-b + pierwiastek) / (2*a)
    print("dwa rozwiazania", x1, x2)
