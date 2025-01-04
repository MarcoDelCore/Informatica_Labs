def main():
    prodotti = open('prodotti.txt', 'r')
    diz_negozi = {}
    for line in prodotti:
        riga = line.rstrip().split()
        diz_negozi[riga[1]] = riga[0]

    acquisti = open('acquisti.txt', 'r')
    diz_acquisti = {}
    sospetti = []
    for line in acquisti:
        riga = line.rstrip().split()
        diz_acquisti[riga[1]] = riga[0]
        for (key, val) in diz_negozi.items():
            if riga[1] != key and riga[0] == val:
                sospetti.append(val)

    print('Elenco transazioni sospette:')
    print()
    for elemento in sospetti:
        print('Codice prodotto:', elemento)
        for (key, val) in diz_negozi.items():
            if val == elemento:
                print("Rivenditore ufficiale:", key)
        print('Lista riivenditori: ', end='')
        for (key, val) in diz_acquisti.items():
            if elemento == val:
                print(key, end=' ')
        print()
        print()

main()