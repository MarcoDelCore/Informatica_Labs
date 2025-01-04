def main():
    labirinto = open("labirinto.txt", "r")
    corridoi = []
    dizionario = {}
    riga = 0
    colonna = 0
    line = labirinto.readline()
    while line != '':
        colonna = 0
        line.rstrip()
        for ch in line:
            if ch.isspace() and colonna <= 8:
                corridoio = (riga, colonna)
                corridoi.append(corridoio)
            colonna += 1
        riga += 1
        line = labirinto.readline()
    print(corridoi)

    for elemento in corridoi:
        (r, c) = elemento
        adiacenti = {(r, c+1), (r+1, c), (r, c-1), (r-1, c)}
        check = adiacenti.copy()
        for coppia in check:
            if coppia not in corridoi:
                adiacenti.remove(coppia)
        dizionario[elemento] = adiacenti
    print(dizionario)


main()
