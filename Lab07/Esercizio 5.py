from random import randint
lista = []
NUM_VALORI = 20
for i in range(0, NUM_VALORI):
    lista.append(randint(0, 99))
print("La sequenza generata è: ", lista)
lista.sort()
print("La sequenza ordinata è: ", lista)