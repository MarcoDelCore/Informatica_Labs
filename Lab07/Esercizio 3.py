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
    eq = equals(lista1, lista2)
    if eq:
        print("Le liste sono identiche.")
    else:
        print("Le liste non sono identiche.")


def equals(a, b):
    controllo = True
    if len(a) == len(b):
        for i in range(len(a)):
            if a[i] != b[i]:
                controllo = False
    else:
        controllo = False
    return controllo

main()
