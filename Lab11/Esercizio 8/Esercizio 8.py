def main():
    labirinto = open("labirinto.txt", "r")
    mappa = open("mappa.txt", "w")
    corridoi = []
    dizionario = {}
    adiacenti = {}
    riga = 0
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

    for elemento in corridoi:
        (r, c) = elemento
        vicino = {(r, c+1), (r+1, c), (r, c-1), (r-1, c)}
        check = vicino.copy()
        for coppia in check:
            if coppia not in corridoi:
                vicino.remove(coppia)
        adiacenti[elemento] = vicino

    for coppia in corridoi:
        dizionario[coppia] = '?'

    for key in dizionario:
        (r, c) = key
        if r == 0:
            dizionario[key] = 'N'
        elif c == 0:
            dizionario[key] = 'W'
        elif r == 8:
            dizionario[key] = 'S'
        elif c == 8:
            dizionario[key] = 'E'

    valori = []
    for (key, val) in dizionario.items():
        valori.append(val)
    while '?' in valori:
        direzioni(dizionario, adiacenti)
        valori = []
        for (key, val) in dizionario.items():
            valori.append(val)

    for (key, val) in dizionario.items():
        if val == 'x':
            dizionario[key] = '?'
    print(dizionario)

    labirinto.close()
    labirinto = open("labirinto.txt", "r")
    riga1 = 0
    line = labirinto.readline()
    while line != '':
        colonna1 = 0
        line.rstrip()
        for ch in line:
            if colonna1 <= 8:
                if ch == '*':
                    mappa.write(ch)
                elif ch.isspace():
                    chiave = (riga1, colonna1)
                    ch = dizionario[chiave]
                    mappa.write(ch)
                colonna1 += 1
        riga1 += 1
        mappa.write('\n')
        line = labirinto.readline()

    labirinto.close()
    mappa.close()


def direzioni(dizionario, adiacenti):
    for (key, val) in dizionario.items():
        (r1, c1) = key
        if val == '?':
            for elemento in adiacenti[key]:
                if dizionario[elemento].isalpha():
                    (r2, c2) = elemento
                    if r1 < r2:
                        dizionario[key] = 'S'
                    elif r1 > r2:
                        dizionario[key] = 'N'
                    elif c1 < c2:
                        dizionario[key] = 'E'
                    elif c1 > c2:
                        dizionario[key] = 'W'
        if val == '?' and adiacenti[key] == set():
            dizionario[key] = 'x'


main()
