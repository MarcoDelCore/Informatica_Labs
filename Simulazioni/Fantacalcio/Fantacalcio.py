def main():
    giocatori = open("statistiche.dat", "r")
    dizionario = {}
    riga = giocatori.readline()

    while riga != '':
        giocatore = riga.split()
        prestazione = float(giocatore[3])*(float(giocatore[4])*0.5 + int(giocatore[5])*0.5
                                           - int(giocatore[6])*0.2 - int(giocatore[7])*0.4)
        giocatore.append(prestazione)
        dizionario[giocatore[0]] = giocatore
        riga = giocatori.readline()

    scelta = input("Valutazione(V) o Confronto(C): ")

    if scelta.upper() == "V":
        ruolo = input("Inseerisci ruolo: ")
        valutazioni = []
        for (key, val) in dizionario.items():
            if val[2] == ruolo.upper():
                valutazioni.append(val[8])
        while len(valutazioni) > 3:
            minimo = valutazioni[0]
            for elemento in valutazioni:
                if float(elemento) < float(minimo):
                    minimo = elemento
            valutazioni.remove(minimo)
        consigliati = []
        for elemento in valutazioni:
            for (key, val) in dizionario.items():
                if elemento in val:
                    consigliati.append(val)
        print("I migliori 3 giocatori per questo ruolo sono: ")
        for elemento in consigliati:
            consigliato = ''
            for i in range(8):
                consigliato = consigliato + ' ' + elemento[i]
            print(consigliato)

    elif scelta.upper() == 'C':
        confronto = input("Inserisci i nomi dei 2 giocatori: ")
        nomi = confronto.split()
        ruolo1 = None
        ruolo2 = None
        for (key, val) in dizionario.items():
            if key == nomi[0]:
                ruolo1 = val[2]
            elif key == nomi[2]:
                ruolo2 = val[2]
        if ruolo1 != ruolo2:
            print("Confronto impossibile.")
        else:
            valutazione1 = None
            valutazione2 = None
            for (key, val) in dizionario.items():
                if key == nomi[0]:
                    valutazione1 = val[8]
                elif key == nomi[2]:
                    valutazione2 = val[8]
            nome = ''
            if valutazione1 > valutazione2:
                for (key, val) in dizionario.items():
                    if key == nomi[0]:
                        for i in range(8):
                            nome = nome + ' ' + val[i]
            else:
                for (key, val) in dizionario.items():
                    if key == nomi[2]:
                        for i in range(8):
                            nome = nome + ' ' + val[i]
            print("Il giocatore migliore è: ", nome)


main()
