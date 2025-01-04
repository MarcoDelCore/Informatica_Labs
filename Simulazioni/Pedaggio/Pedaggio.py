def main():
    tratte = open("pedaggi.txt", "r")
    partenza = input("Inserire città di partenza: ")
    arrivo = input("Inserisre città di arrivo: ")

    if partenza == arrivo:
        print("Errore: città di partenza e di arrivo coincidono.")
    else:
        dizionario = {}
        for line in tratte:
            temp = line.split(';')
            tratta = (temp[0], temp[1])
            dizionario[tratta] = float(temp[2])

        for (key, val) in dizionario.items():
            (part, arr) = key
            if partenza == part:
                if arrivo == arr:
                    spesa = val
                    print("Destinazione raggiunta in 1 tratta. Spesa complessiva: %.2f euro" % spesa)
                else:
                    spesa = val
                    intermedio = arr
                    for (key, val) in dizionario.items():
                        (part, arr) = key
                        if part == intermedio:
                            if arr == arrivo:
                                spesa += val
                                print("Destinazione raggiunta in 2 tratte. Spesa complessiva: %.2f euro" % spesa)
                            else:
                                spesa += val
                                intermedio = arr
                                for (key, val) in dizionario.items():
                                    (part, arr) = key
                                    if part == intermedio:
                                        if arr == arrivo:
                                            spesa += val
                                            print("Destinazione raggiunta in 3 tratte. Spesa complessiva: %.2f euro" % spesa)
                                        else:
                                            print("Impossibile raggiungere la destinazione percorrendo un massimo"
                                                  "di 3 tratte.")


main()
