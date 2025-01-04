def main():
    lista1 = []
    valore_str = input("Inserisci un valore per la prima lista: ")
    while valore_str != '':
        lista1.append(int(valore_str))
        valore_str = input("Inserisci un altro valore o INVIO per uscire: ")
    lista2 = []
    valore_str = input("Inserisci un valore per la seconda lista: ")
    while valore_str != '':
        lista2.append(int(valore_str))
        valore_str = input("Inserisci un altro valore o INVIO per uscire: ")
    print("Le liste date sono: ")
    print(lista1)
    print(lista2)
    ordinata = mergeSorted(lista1, lista2)
    print("Le liste fuse e ordinate sono: ", ordinata)



#def mergeSorted(l1, l2):