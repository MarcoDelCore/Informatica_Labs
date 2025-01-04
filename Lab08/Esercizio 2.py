def main():
    tabella = []
    colonne = int(input("Inserisci il numero di colonne della tabella: "))
    righe = int(input("Inserisci il numero di righe della tabella: "))
    for i in range(righe):
        temp = []
        for j in range(colonne):
            temp.append(float(input("Inserisci valore: ")))
        tabella.append(temp)
    print("La tabella creata è la seguente:")
    for i in range(righe):
        for j in range(colonne):
            print("%5d" % tabella[i][j], end='')
        print()
    riga = int(input(f"Inserire riga (0,{righe - 1}): "))
    colonna = int(input(f'inserire colonna (0, {colonne - 1}): '))
    media = media_vicini(tabella, riga, colonna)
    print("La media dei vicini è %.2f" % media)


def media_vicini(tab, riga, colonna):
    somma = 0
    contatore = 0
    if riga == 0 and colonna == 0:
        for i in range(riga + 2):
            for j in range(colonna + 2):
                somma = somma + tab[i][j]
                contatore += 1

    elif riga == 0 and colonna != len(tab) - 1:
        for i in range(riga + 2):
            for j in range(colonna - 1, colonna + 2):
                somma = somma + tab[i][j]
                contatore += 1

    elif riga == 0 and colonna == len(tab) - 1:
        for i in range(riga + 2):
            for j in range(colonna - 1, colonna + 1):
                somma += tab[i][j]
                contatore += 1

    elif riga != len(tab[riga]) - 1 and colonna == 0:
        for i in range(riga - 1, riga + 2):
            for j in range(colonna + 2):
                somma += tab[i][j]
                contatore += 1

    elif riga == len(tab[riga]) - 1 and colonna == 0:
        for i in range(riga - 1, riga + 1):
            for j in range(colonna + 2):
                somma += tab[i][j]
                contatore += 1

    elif riga != len(tab[riga]) - 1 and colonna == len(tab) - 1:
        for i in range(riga - 1, riga + 2):
            for j in range(colonna - 1, colonna + 1):
                somma += tab[i][j]
                contatore += 1

    elif riga == len(tab[riga]) - 1 and colonna != len(tab) - 1:
        for i in range(riga - 1, riga + 1):
            for j in range(colonna - 1, colonna + 2):
                somma += tab[i][j]
                contatore += 1

    elif riga == len(tab[riga]) - 1 and colonna == len(tab) - 1:
        for i in range(riga - 1, riga + 1):
            for j in range(colonna - 1, colonna + 1):
                somma += tab[i][j]
                contatore += 1

    else:
        for i in range(riga - 1, riga + 2):
            for j in range(colonna - 1, colonna + 1):
                somma += tab[i][j]
                contatore += 1

    media = (somma - tab[riga][colonna])/(contatore - 1)
    return media


main()
