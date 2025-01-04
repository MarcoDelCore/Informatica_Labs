
def main():
    presenze = open("presenze.txt", "r")
    sospetti = open("sospetti.txt", "r")

    sosp = []
    for line in sospetti:
        line = line.rstrip()
        sosp.append(line)

    dizionario = {}
    for line in presenze:
        line = line.rstrip().split(',')
        dizionario[line[0]] = [line[1], line[2], line[3]]

    for elemento in sosp:
        presente = False
        print(f"*** Contatti del cliente: {elemento}: ***")
        trovato = False
        contatti = []
        for (key, val) in dizionario.items():
            if elemento == key:
                presente = True
                arrivo = int(val[1])
                partenza = int(val[2])
                for (key1, val1) in dizionario.items():
                    if key1 != elemento:
                        if (arrivo <= int(val1[1]) <= partenza) or (arrivo <= int(val1[2]) <= partenza) or \
                                (int(val1[1]) <= arrivo and int(val1[2]) >= partenza):
                            trovato = True
                            contatti.append(key1)

                contatti.sort()
                for contatto in contatti:
                    print(f"- Contatto con {contatto}, telefono {dizionario[contatto][0]}")
        if not presente:
            print(f"{elemento} non è presente nel database.")
        if not trovato and presente:
            print(f"{elemento} non ha avuto contatti con nessuno.")
        print()

    sospetti.close()
    presenze.close()


main()
