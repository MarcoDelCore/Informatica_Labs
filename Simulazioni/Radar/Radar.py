def main():

    mappa = open("mappa.txt", "r")
    tabella = []

    riga = mappa.readline()
    while riga != '':
        temp = []
        riga.rstrip()
        for ch in riga:
            if not ch.isspace():
                temp.append(ch)
        tabella.append(temp)
        riga = mappa.readline()
    mappa.close()
    for i in range(len(tabella)):
        for j in range(len(tabella[i])):
            print("%3s" % tabella[i][j], end='')
        print()

    dizionario_colonna = {}
    dizionario_riga = {}

    colonna = 0
    while colonna < len(tabella[0]):
        ostacolo_colonna = 0
        for riga in range(len(tabella)):
            if tabella[riga][colonna] == '1':
                ostacolo_colonna += 1
                if riga < len(tabella) - 1 and tabella[riga + 1][colonna] != '1' \
                        or riga == len(tabella) - 1:
                    dizionario_colonna[colonna] = ostacolo_colonna
                    ostacolo_colonna = 0
        colonna += 1

    riga = 0
    while riga < len(tabella):
        ostacolo_riga = 0
        for colonna in range(len(tabella[0])):
            if tabella[riga][colonna] == '1':
                ostacolo_riga += 1
                if colonna < len(tabella[0]) - 1 and tabella[riga][colonna + 1] != '1'\
                        or colonna == len(tabella[0]) - 1:
                    dizionario_riga[riga] = ostacolo_riga
                    ostacolo_riga = 0
        riga += 1

    massimo_riga = dizionario_riga[0]
    rig = 0
    for (key, val) in dizionario_riga.items():
        if val > massimo_riga:
            massimo_riga = val
            rig = key

    massimo_colonna = dizionario_colonna[0]
    col = 0
    for (key, val) in dizionario_colonna.items():
        if val > massimo_colonna:
            massimo_colonna = val
            col = key

    diz = {}
    pos_col = []
    for i in range(len(tabella)):
        for elemento in tabella[i][col]:
            pos = (i, col)
            pos_col.append(pos)
    diz[col] = pos_col

    pos_riga = []
    for i in range(len(tabella[0])):
        for elemento in tabella[rig][i]:
            pos = (rig, i)
            pos_riga.append(pos)
    diz[rig] = pos_riga

    trovato = False
    riga_comune = 0
    colonna_comune = 0
    for i in diz[col]:
        for j in diz[rig]:
            if i == j:
                trovato = True
                (riga_comune, colonna_comune) = i

    print(f"Ostacolo massimo di dimensione {massimo_riga} posizionato sulla riga {rig}.")
    print(f"Ostacolo massimo di dimensione {massimo_colonna} posizionato sulla colonna {col}.")

    if trovato:
        print(f"Gli ostacoli hanno un punto in comune in posizione riga {riga_comune} colonna {colonna_comune}")
    else:
        print("Gli ostacoli non hanno elementi in comune.")


main()
