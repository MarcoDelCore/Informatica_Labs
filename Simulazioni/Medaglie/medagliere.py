def main():
    medagliere = open("nazioni.txt", "r")

    dizionario = {}
    for line in medagliere:
        riga = line.rstrip().split()
        if riga[2] not in dizionario:
            dizionario[riga[2]] = riga[3]
        else:
            temp = [riga[3]]
            for elemento in dizionario[riga[2]]:
                temp.append(elemento)
            dizionario[riga[2]] = temp

    for (key, val) in dizionario.items():
        medal = 0
        for element in val:
            if element == '1':
                medal += 1
            elif element == '2':
                medal += 0.1
            elif element == '3':
                medal += 0.05
        dizionario[key] = medal

    print("Medaglie d'oro equivalenti:")
    for key in dizionario:
        val = float(dizionario[key])
        val = round(val, 2)
        print(f"{key} {val}")

    print()

    top = []
    for (key, val) in dizionario.items():
        top.append(val)

    top.sort(reverse=True)

    print("Le prime tre nazioni del medagliere sono:")
    i = 1
    for elemento in top:
        if i <= 3:
            for (key, val) in dizionario.items():
                if val == elemento:
                    print("%3d) " % i, key)
        i += 1


main()
