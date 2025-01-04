# Scrivete un programma che legga un numero intero, n, e visualizzi usando asterischi,
# un quadrato e un rombo pieni il cui lato abbia lunghezza n
n = int(input("Inserisci un valore: "))

for i in range(0, n):
    for j in range(0, n):
        print("*", end='')
    print()

print()

for i in range(1, n + 1):
    print(' ' * (n - i) + '*' * ((2 * i) - 1) + ' ' * (n - i))
for i in range(n - 1, 0, -1):
    print(' ' * (n - i) + '*' * ((2 * i) - 1) + ' ' * (n - i))
