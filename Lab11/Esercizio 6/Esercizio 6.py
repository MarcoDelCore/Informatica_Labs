def main():
    dizionario = {}
    dati = open("rawdata_2004.txt", "r")
    line = dati.readline()
    while line != '':
        parti = line.rstrip().split()
        dizionario[parti[1]] = parti[2]
        line = dati.readline()
    print(dizionario)

    nazione = input("Inserisci il nome di una nazione: ")
    while nazione.lower() != 'quit':
        if nazione in dizionario:
            print(f'Il reddito annuo pro capite di {nazione} è di {dizionario[nazione]}')
        else:
            print("Errore. Controlla di aver scritto correttamente il nome della nazione desiderata.")
            print("Ricorda che il primo carattere deve essere maiuscolo!")
        nazione = input(("Inserisci il nome di una nazione o \'quit\': "))


main()
