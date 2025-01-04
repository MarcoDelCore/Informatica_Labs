def main():
    lista = []
    valore = input("Inserisci un valore: ")
    while valore != '':
        lista.append(int(valore))
        valore = input("Inserisci un valore o INVIO per uscire: ")
    print("La lista data è: ", lista)
    removemin(lista)


def removemin(lista):
    minimo = lista[0]
    new = []
    for i in range(1, len(lista)):
        if lista[i] < minimo:
            new.append(minimo)
            minimo = lista[i]
        else:
            new.append(lista[i])
    print("La lista senza il minimo è: ", new)


main()
