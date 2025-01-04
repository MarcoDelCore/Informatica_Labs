# Scrivete un programma che legga una parola e visualizzi tutte le sue sottostringhe,
# ordinate per lunghezza crescente.
stringa = input("Inserisci una stringa: ")
lunghezza = len(stringa)
contatore = 0
while contatore < lunghezza-1:
    for i in range(0, lunghezza):
        if i - contatore >= 0:
            print (stringa[i-contatore:i+1])
    contatore = contatore + 1
