def main():
    lista = []
    numero = input("Inserisci un numero: ")
    while numero != '':
        numero = int(numero)
        lista.append(numero)
        numero = input("Inserisci un numero o premi INVIO per uscire: ")
    somma_alternata = SommaAlternata(lista)
    print("La somma alternata degli elementi della lista è: ", somma_alternata)


def SommaAlternata(lista):
    somma = 0
    for i in range(len(lista)):
        if i % 2 == 0:
            somma = somma + lista[i]
        else:
            somma = somma - lista[i]
    return somma


main()
