print("-ESERCIZIO 6-")
numero = input("Inserisci il primo numero: ")
n = int(numero)
totale = 0
contatore = 1
while contatore <= 10:
    totale = totale + n
    n = n + 1
    contatore = contatore + 1
print("La somma dei primi 10 numeri positivi a partire da", numero, "è", totale)
