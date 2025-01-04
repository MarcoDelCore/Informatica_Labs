import random


def main():
    table = [
        [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
        [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
        [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
        [10, 10, 20, 20, 20, 20, 20, 20, 10, 10],
        [10, 10, 20, 20, 20, 20, 20, 20, 10, 10],
        [10, 10, 20, 20, 20, 20, 20, 20, 10, 10],
        [20, 20, 30, 30, 40, 40, 30, 30, 20, 20],
        [20, 30, 30, 40, 50, 50, 40, 30, 30, 20],
        [30, 40, 50, 50, 50, 50, 50, 50, 40, 30]
                    ]
    stampatabella(table)
    while not full(table):
        scelta = input("Scegliere posto o prezzo? ")
        if scelta == "prezzo":
            prezzo = int(input("Inserisci il prezzo: "))
            if controlloprezzo(table, prezzo):
                sceltaprezzo(table, prezzo)
            else:
                print("Non ci sono posti disponibili a questo prezzo.")
        elif scelta == "posto":
            fila = int(input("Inserire numero fila (0-8): "))
            colonna = int(input("Inserire colonna (0-9): "))
            if controlloposto(table, fila, colonna):
                sceltaposto(table, fila, colonna)
            else:
                print("Il posto selezionato non è disponibile.")

        stampatabella(table)
    print("Biglietti esauriti.")


def stampatabella(tab):
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            print("%4d" % tab[i][j], end='')
        print()


def controlloprezzo(tab, prezzo):
    temp = []
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            temp.append(tab[i][j])
    if prezzo in temp:
        return True
    else:
        return False


def sceltaprezzo(tab, prezzo):
    riga = random.randint(0, 8)
    colonna = random.randint(0, 9)
    posto = tab[riga][colonna]
    while posto != prezzo:
        riga = random.randint(0, 8)
        colonna = random.randint(0, 9)
        posto = tab[riga][colonna]
    print("Lè è stato assegnato il posto in %d fila e %d colonna." % (riga, colonna))
    tab[riga][colonna] = 0


def controlloposto(tab, riga, colonna):
    if tab[riga][colonna] != 0:
        return True
    else:
        return False


def sceltaposto(tab, riga, colonna):
    print("Il posto selezionato ha un costo di %d dollari." % tab[riga][colonna])
    tab[riga][colonna] = 0


def full(tab):
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            if tab[i][j] != 0:
                return False
    return True


main()
