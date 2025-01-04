def main():
    lista1 = []
    numero = input("Inserisci un valore per la prima lista: ")
    while numero != '':
        lista1.append(numero)
        numero = input("Inserisci un altro valore o INVIO per uscire: ")
    lista2 = []
    valore = input("Inserisci un valore per la seconda lista: ")
    while valore != '':
        lista2.append(valore)
        valore = input("Inserisci un altro valore o INVIO per uscire: ")
    print("Prima lista: ", lista1)
    print("Seconda lista: ", lista2)
    corrispondenza = sameSet(lista1, lista2)
    if corrispondenza:
        print("Le due liste contengono gli stessi elementi.")
    else:
        print("Le due liste NON contengono gli stessi elementi.")


def sameSet(a, b):
    for element in a:
        if element not in b:
            return False
    for element in b:
        if element not in a:
            return False
    return True

main()