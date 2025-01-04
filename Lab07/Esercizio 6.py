def main():
    lista = []
    numero = input("Inserisci un numero: ")
    while numero != '':
        numero = int(numero)
        lista.append(numero)
        numero = input("Inserisci un numero o premi INVIO per uscire: ")
    print("La lista è: ", lista)
    InvertiLista(lista)
    print("La lista invertita è: ", lista)

def InvertiLista(a):
    for i in range(len(a) // 2):
        temp = a[i]
        a[i] = a[len(a) - 1 - i]
        a[len(a) - 1 - i] = temp


main()
