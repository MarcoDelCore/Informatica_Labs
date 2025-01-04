def main():
    elenco_classi = open("classes.txt", "r")
    voti = open("voti.txt", "w")

    classe = []

    studente = input("Inserisci ID: ")
    voti.write("student ID" + studente + "\n")

    for line in elenco_classi:
        classe.append(line.rstrip("\n"))

    for elemento in classe:
        nome = elemento + ".txt"
        try:
            file = open(nome, "r")
            for riga in file:
                riga = riga.split()
                if studente == riga[0]:
                    voti.write(elemento + " " + riga[1] + "\n")
            file.close()
        except:
            print("Non ha sostenuto l'esame.")

    elenco_classi.close()
    voti.close()


main()
