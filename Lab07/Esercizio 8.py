def main():
    lista = []
    numero = input("Inserisci un numero: ")
    while numero != '':
        numero = float(numero)
        lista.append(numero)
        numero = input("Inserisci un numero o premi INVIO per uscire: ")
    print("La lista data è: ", lista)
    mediata = CorrezioneValori(lista)
    print("La lista corretta è: ", mediata)


def CorrezioneValori(lista):
    a = []
    for i in range(len(lista)):
        if i == 0:
            a.append((lista[i] + lista[i + 1]) / 2)
        elif i == (len(lista) - 1):
            a.append((lista[i] + lista[i - 1]) / 2)
        elif i > 1:
            a.append((lista[i] + lista[i + 1] + lista[i - 1]) / 3)
    return a



main()
