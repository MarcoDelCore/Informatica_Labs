def main():
    parolacce = open("parolacce.txt", "r")
    censurare = set()
    line = parolacce.readline()
    while line != '':
        censurare.add(line.rstrip())
        line = parolacce.readline()
    parolacce.close()

    testo = open("input.txt", "r")
    out = open("output.txt", "w")
    line = testo.readline()
    while line != '':
        parole = line.rstrip().split()
        for parola in parole:
            if parola in censurare:
                parola = '*' * len(parola)
            out.write(parola + ' ')
        out.write('\n')
        line = testo.readline()


main()
