def main():
    lista = []
    valore = input("Inserisci un valore: ")
    while valore != '':
        valore = int(valore)
        lista.append(valore)
        valore = input("Inserisci un nuovo valore o INVIO per uscire: ")
    print("La lista data è: ", lista)
    somma = SumWithoutSmallest(lista)
    print("La differenza tra la somma senza il valore minimo e il valore minimo è: ", somma)


def SumWithoutSmallest(lista):
    minimo = lista[0]
    somma = 0
    for elemento in lista:
        if elemento < minimo:
            minimo = elemento
        somma = somma + elemento
    print("La somma è: ", somma)
    print("Il valore minimo è: ", minimo)
    return somma - minimo


main()
