# Usando la formula seguente:
# rnew = (a ⋅ rold + b) % m
# e, poi, assegnando rnew a rold, si ottiene un semplice generatore casuale.
# Scrivete un programma che chieda all’utente di fornire un valore iniziale per rold
# (valore che viene chiamato “seme”, seed), poi visualizzi i primi 100 numeri interi
# generati dalla formula, usando a = 32310901, b = 1729 e m = 2^24
a = 32310901
b = 1729
m = 2**24
seme = int(input("Inserisci un numero: "))
r_old = seme
for i in range (1, 101):
    r_new = (a * r_old + b) % m
    r_old = r_new
    print(i, " " * (4 - len(str(i))), r_new)