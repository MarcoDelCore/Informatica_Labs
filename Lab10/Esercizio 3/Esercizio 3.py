def main():
    files = []
    word = input("Inserisci parola da cercare: ")
    name = input("Inserisci nome file: ")
    while name != '':
        files.append(name)
        name = input("Inserisci nome file: ")
    print(files)
    out = open("output.txt", "w")
    for element in files:
        testo = open(element, "r")
        riga = testo.readline()
        while riga != '':
            if word.upper() in riga.upper():
                out.write(element + ":" + riga)
            riga = testo.readline()
        testo.close()
    out.close()


main()