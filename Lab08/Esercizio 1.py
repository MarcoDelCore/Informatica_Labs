def main():
    lista1 = []
    valore_str = input("Inserisci un valore per la prima lista: ")
    while valore_str != '':
        lista1.append(valore_str)
        valore_str = input("Inserisci un altro valore o INVIO per uscire: ")
    lista2 = []
    valore_str = input("Inserisci un valore per la seconda lista: ")
    while valore_str != '':
        lista2.append(valore_str)
        valore_str = input("Inserisci un altro valore o INVIO per uscire: ")
    print("Le liste date sono: ")
    print(lista1)
    print(lista2)
    print("Le due liste \"fuse\" sono: ", end='')
    merge(lista1, lista2)


def merge(l1, l2):
    if len(l1) > len(l2):
        for i in range(len(l2)):
            print(l1[i], l2[i], end=' ')
        for i in range(len(l2), len(l1)):
            print(l1[i], end=' ')
    elif len(l1) < len(l2):
        for i in range(len(l1)):
            print(l1[i], l2[i], end=' ')
        for i in range(len(l1), len(l2)):
            print(l2[i], end=' ')
    elif len(l1) == len(l2):
        for i in range(len(l1)):
            print(l1[i], l2[i], end=' ')


main()
