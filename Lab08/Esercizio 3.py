def main():
    tabella = []
    dimensione = 4
    righe = colonne = dimensione
    check = []
    for i in range(righe):
        temp = []
        for j in range(colonne):
            valore = float(input(f"Inserisci valore compreso tra 1 e {dimensione**2}: "))
            while valore < 1 or valore > dimensione**2 or valore in check:
                print("Valore non valido.")
                valore = float(input(f"Inserisci valore compreso tra 1 e {dimensione**2}: "))
            temp.append(valore)
            check.append(valore)
        tabella.append(temp)
    print("La tabella creata è la seguente:")
    for i in range(dimensione):
        for j in range(dimensione):
            print("%5d" % tabella[i][j], end='')
        print()





main()