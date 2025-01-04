def main():
    dati = open("dati.txt", "r")
    importi = open("importi.txt", "w")
    line = dati.readline()
    while line != '':
        importo = line.split()
        print(importo)
        if importo[0].rstrip("; ").isalpha() and importo[1].rstrip("; ").isalpha() and \
                importo[2].rstrip("; ").isdigit():
            importi.write(importo[0].rstrip(";") + ":" + importo[2].strip(";") + "\n")
        else:
            print("Formato non corretto.")
        line = dati.readline()
    dati.close()
    importi.close()


main()
