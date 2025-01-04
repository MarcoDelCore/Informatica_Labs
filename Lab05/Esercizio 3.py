# Fattorizzazione di interi. Scrivete un programma che chieda all’utente un numero
# intero e ne visualizzi i fattori.
numero = int(input("Inserire un numero: "))
for i in range(2, numero+1):
    for j in range (2, i):
        if numero % j == 0:
            print(j)
            numero = numero / j
print("-----OPPURE-----")
numero = int(input("Inserire un numero: "))
x = 2
while x <= numero:
    if numero % x == 0:
        print(x)
        numero = numero / x
        x = 1
    x = x + 1
