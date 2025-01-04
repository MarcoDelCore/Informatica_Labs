from random import randint
lista = []
contatore = 1
while contatore <= 10:
    numero = randint(0, 100)
    lista.append(numero)
    contatore += 1
print(lista)

print("Gli elementi di indice pari sono: ", end='')
for i in range(len(lista)):
    if i % 2 == 0:
        print(lista[i], end='   ')
print()

print("Gli elementi di valore pari sono: ", end='')
for i in range(len(lista)):
    if lista[i] % 2 == 0:
        print(lista[i], end='   ')
print()

print("Gli elementi in ordine inverso: ", end=' ')
for i in range(len(lista) - 1, -1, -1):
    print(lista[i], end=' ')
print()

print("Il primo elemento della lista è: ", lista[0])
print("L'ultimo elemento della lista è: ", lista[len(lista) - 1])
