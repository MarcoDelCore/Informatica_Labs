def main():
    chiave = input("Inserisci una parola chiave: ")
    chiave = eliminadoppie(chiave)
    chiave = chiave.upper()

    alfabeto = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
                "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X",
                "Y", "Z"]

    cifrato = []

    for lettera in chiave:
        cifrato.append(lettera)

    for i in range(len(alfabeto) - 1, -1, -1):
        if alfabeto[i] not in cifrato:
            cifrato.append(alfabeto[i])

    scelta = input("Cifrare o decifrare (C/D)? ")

    inputFile = "input.txt"
    outputFile = "output.txt"

    if scelta.upper() == "D":
        cifratura(inputFile, outputFile,cifrato, alfabeto)
    elif scelta.upper() == "C":
        cifratura(inputFile, outputFile, alfabeto, cifrato)


def eliminadoppie(parola):
    new = ''
    for lettera in parola:
        if lettera not in new:
            new = new + lettera
    return new


def cifratura(infile, outfile, alfabeto, cifrario):
    try:
        testo = open(infile, "r")
        cifrato = open(outfile, "w")
    except:
        print("File non trovato")
        return

    for riga in testo:
        for carattere in riga:
            if carattere.isalpha():
                indice = cercaIndice(carattere.upper(), alfabeto)
                if carattere.isupper():
                    carattere_cifrato = cifrario[indice]
                else:
                    carattere_cifrato = cifrario[indice].lower()
                cifrato.write(carattere_cifrato)
            else:
                cifrato.write(carattere)
    testo.close()
    cifrato.close()


def cercaIndice(lettera, alfabeto):

    for i in range(len(alfabeto)):
        if alfabeto[i] == lettera:
            return i


main()
