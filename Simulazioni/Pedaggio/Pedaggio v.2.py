def main():
    partenza = input("Inserire città di partenza: ")

    while partenza != '':
        arrivo = input("Inserisre città di arrivo: ")

        if partenza == arrivo:
            print("Errore: città di partenza e di arrivo coincidono.")
        else:
            dizionario = {}
            tratte = open("pedaggi.txt", "r")
            for line in tratte:
                temp = line.split(';')
                tratta = (temp[0], temp[1])
                dizionario[tratta] = float(temp[2])

            check_partenza = False
            check_arrivo = False
            for (key, val) in dizionario.items():
                (part, arr) = key
                if part == partenza:
                    check_partenza = True
                if arr == arrivo:
                    check_arrivo = True

            if check_partenza and check_arrivo:
                n = 1
                trovato = False
                spesa = 0
                while n <= 3 and not trovato:
                    for (key, val) in dizionario.items():
                        (part, arr) = key
                        if part == partenza:
                            spesa += val
                            if arr == arrivo:
                                trovato = True
                            else:
                                partenza = arr
                                n += 1

                if trovato:
                    print(f"Destinazione raggiunta in {n} tratte. Spesa complessiva: %.2f euro" % spesa)
                else:
                    print("Impossibile raggiungere la tratta in un massimo di 3 tratte.")
            else:
                print("Errore nel calcolo del tragitto. Una delle città non è presente.")

            tratte.close()

        partenza = input("Inserire città di partenza o INVIO per uscire: ")


main()
