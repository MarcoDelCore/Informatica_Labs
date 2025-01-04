def main():
    chiave = input("Inserisci una parola chiave: ")
    chiave = eliminadoppie(chiave)
    chiave = chiave.upper()

    alfabeto = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "K", "L",
                "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X",
                "Y", "Z"]

    cifrato = []

    for lettera in chiave:
        cifrato.append(lettera)

    for i in range(len(alfabeto)):
        if alfabeto[i] not in cifrato:
            cifrato.append(alfabeto[i])

    tabella = []
    for i in range(len(cifrato)):
        if (i + 1) % 5 == 0:
            temp = cifrato[i-4:i+1]
            tabella.append(temp)

    infile = open("input.txt", "r")
    outfile = open("output.txt", "w")

    testo = infile.read()
    testo = testo.replace("J", "I")
    testo = testo.replace("j", "i")

    check = eliminacaratteri(testo)
    surplus = False
    if len(check) % 2 != 0:
        surplus = True
        testo = testo + "z"
    print(testo)
    i = 0
    infile2 = open("input.txt", "r")
    riga = infile2.readline()
    while i < len(testo):
        if i == (len(riga) - 1):
            outfile.write("\n")
            riga = infile2.readline()
        extra = ''
        if testo[i].isalpha():
            if testo[i].islower():
                low1 = True
                carattere1 = testo[i]
                i += 1
                if i == (len(riga) - 1):
                    outfile.write("\n")
                    riga = infile2.readline()
                while not testo[i].isalpha():
                    extra = extra + testo[i]
                    i += 1
                if testo[i].islower():
                    low2 = True
                    carattere2 = testo[i]
                    (r1, c1) = cercaindici(carattere1, tabella)
                    (r2, c2) = cercaindici(carattere2, tabella)
                    (carattere1, carattere2) = cifratura(r1, r2, c1, c2, tabella)

                    if low1:
                        carattere1 = carattere1.lower()
                    if low2:
                        carattere2 = carattere2.lower()
                    if surplus and i == len(testo) - 1:
                        outfile.write(carattere1+extra)
                    elif i == len(riga) - 1:
                        outfile.write(carattere1+extra+carattere2+"\n")
                        riga = infile2.readline()
                    else:
                        outfile.write(carattere1+extra+carattere2)




        i += 1



def cifratura(r1, r2, c1, c2, tab):
    if (r1 == r2 and c1 == c2) or (r1 != r2 and c1 != c2) or (r1 == r2 and c1 != c2):
        car1 = tab[r1][c2]
        car2 = tab[r2][c1]
    else:
        car1 = tab[r2][c1]
        car2 = tab[r1][c2]
    return (car1, car2)


def eliminadoppie(parola):
    new = ''
    for lettera in parola:
        if lettera not in new:
            new = new + lettera
    return new


def cercaindici(carattere, tabella):
    for i in range(5):
        for j in range(5):
            if carattere.upper() == tabella[i][j]:
                return (i, j)
    return(-1, -1)


def eliminacaratteri(testo):
    new = ''
    for ch in testo:
        if ch.isalpha():
            new = new + ch
    return new




main()
