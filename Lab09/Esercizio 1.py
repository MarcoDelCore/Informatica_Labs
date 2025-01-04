def main():
    lista = []
    input_str = input("Inserisci un valore: ")
    while input_str != '':
        lista.append(int(input_str))
        input_str = input("Inserisci un valore o INVIO per uscire: ")
    print("La lista creata è: ", lista)
    print("SCEGLI LA TUA FUNZIONE: \na. Scambiare tra loro il primo e l’ultimo elemento della lista."
          " \nb. Far scorrere tutti gli elementi di una posizione “verso destra”, spostando l’ultimo "
          "elemento nella prima posizione. Ad esempio, la lista 1 4 9 16 25 deve diventare 25 1 4 9 16."
          "\nc. Sostituire con 0 tutti gli elementi di valore pari. \nd. Sostituire ciascun elemento, tranne"
          " il primo e l’ultimo, con il più grande dei due elementi ad esso adiacenti. \ne. Eliminare l’elemento"
          " centrale della lista se questa ha dimensione dispari,altrimenti eliminare i due elementi centrali. "
          "\nf. Spostare tutti gli elementi pari all’inizio della lista (lasciando quelli dispari in coda),"
          " preservando però l’ordinamento relativo tra gli elementi. \ng. Restituire il secondo valore"
          " maggiore della lista. \nh. Restituire True se e solo se la lista è ordinata in senso crescente."
          "\ni. Restituire True se e solo se la lista contiene due elementi adiacenti duplicati."
          "\nj. Restituire True se e solo se la lista contiene elementi duplicati (non necessariamente adiacenti).")
    scelta = input("Inserire la lettera corrispondente alla funzione desiderata: ")
    while scelta != '':
        copia = list(lista)
        if scelta == "a":
            primoultimo(copia)
        elif scelta == "b":
            spostaversodestra(copia)
        elif scelta == "c":
            pariugualezero(copia)
        elif scelta == "d":
            scambiogrande(copia)
        elif scelta == "e":
            eliminacentro(copia)
        elif scelta == "f":
            pariprima(copia)
        elif scelta == "g":
            secondomaggiore(copia)
        elif scelta == "h":
            ordine(copia)
        elif scelta == "i":
            if duplicatiadiacenti(copia):
                print("Ci sono dei duplicati adiacenti.")
            else:
                print("Non ci sono duplicati adiacenti.")
        elif scelta == "j":
            if duplicati(copia):
                print("Ci sono duplicati.")
            else:
                print("Non ci sono duplicati.")
        scelta = input("Inserire la lettera corrispondente alla funzione desiderata o INVIO per uscire: ")


def primoultimo(l):
    (l[0], l[len(l) - 1]) = (l[len(l) - 1], l[0])
    print(l)


def spostaversodestra(l):
    for i in range(1, len(l)):
        (l[i], l[0]) = (l[0], l[i])
    print(l)


def pariugualezero(l):
    for i in range(len(l)):
        if l[i] % 2 == 0:
            l[i] = 0
    print(l)


def scambiogrande(l):
    for i in range(1, len(l) - 1):
        massimo = max(l[i], l[i - 1], l[i + 1])
        l[i] = massimo
    print(l)


def eliminacentro(l):
    if len(l) % 2 != 0:
        l.pop((len(l) // 2))
    else:
        l.pop((len(l) // 2) - 1)
        l.pop(len(l) // 2)
    print(l)


def pariprima(l):
    trovato = 0
    for i in range(len(l)):
        if l[i] % 2 == 0:
            l.insert(0 + trovato, l[i])
            l.pop(i + 1)
            trovato += 1
    print(l)


def secondomaggiore(l):
    massimo = max(l)
    indice = l.index(massimo)
    l.pop(indice)
    nuovomax = max(l)
    print(nuovomax)


def ordine(l):
    controllo = sorted(l)
    if l == controllo:
        print("La lista è ordinata.")
    else:
        print("La lista non è ordinata.")


def duplicatiadiacenti(l):
    trovato = False
    for i in range(1, len(l)):
        if l[i] == l[i - 1]:
            trovato = True
    return trovato


def duplicati(l):
    trovato = 0
    for i in range(len(l)):
        for j in range(len(l)):
            if l[i] == l[j]:
                trovato += 1
    if trovato > len(l):
        return True
    else:
        return False


main()