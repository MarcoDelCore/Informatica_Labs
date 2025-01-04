def main():
    testo = open("input.txt", "r")
    out = open("output.txt", "w")
    riga = testo.readline()
    contatore = 1
    while riga != '':
        out.write("\\*%d*\\" % contatore + riga)
        riga = testo.readline()
        contatore += 1
    testo.close()
    out.close()


main()
