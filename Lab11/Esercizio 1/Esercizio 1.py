def main():
    infile = "input.txt"
    testo = open(infile, "r")
    parole = []

    for line in testo:
        words = line.rstrip().split()
        for elemento in words:
            parole.append(elemento)
    insieme = set(parole)
    print(insieme)
    testo.close()

    dizionario = {}
    ripetizioni = set()

    testo = open(infile, "r")
    for i in insieme:
        contatore = 0
        line = testo.readline()
        while line != '':
            parti = line.rstrip().split()
            for element in parti:
                if element == i:
                    contatore += 1
            line = testo.readline()
        print(f"La parola {i} è ripetuta {contatore} volte.")
        dizionario[i] = contatore
        ripetizioni.add(contatore)
        testo.close()
        testo = open(infile, "r")

    print(dizionario)
    reps = sorted(ripetizioni, reverse=True)
    print(reps)


    print("Le 100 parole più comuni sono: ")
    indice = 1
    for i in reps:
        for (key, val) in dizionario.items():
            if val == i:
                if indice <= 100:
                    print("%-3d: %s" %(indice, key))
                    indice += 1


main()
