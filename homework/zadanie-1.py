#  Napisz program do obliczania silni:
# 1. z wykorzystaniem konstrukcji for
# 2. z wykorzystaniem konstrukcji while
# 3. z wykorzystaniem funkcji. Należy zdefiniować funkcję, która będzie wywoływana rekurencyjnie.

# Ad. 1
def silniaFor(n):
    silnia = 1
    for i in range(1, n + 1): # range(1, n + 1) - od 1 do n włącznie
        silnia *= i
    return silnia

# Ad. 2
def silniaWhile(n):
    silnia = 1
    i = 1
    while i <= n:
        silnia *= i
        i += 1
    return silnia

# Ad. 3
def silniaRekurencyjnie(n):
    if n == 0:
        return 1
    else:
        return n * silniaRekurencyjnie(n - 1)

n = 5
print(f"Silnia z {n} wynosi:")
print(f"1. {silniaFor(n)}")
print(f"2. {silniaWhile(n)}")
print(f"3. {silniaRekurencyjnie(n)}")