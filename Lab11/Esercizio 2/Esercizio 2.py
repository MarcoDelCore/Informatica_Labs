def main():
    stringa1 = input("Inseerisci la prima stringa: ")
    stringa2 = input("Inserisci la seconda stringa: ")
    insieme1 = set()
    insieme2 = set()
    for carattere in stringa1:
        if not carattere.isspace():
            insieme1.add(carattere.upper())
    for carattere in stringa2:
        if not carattere.isspace():
            insieme2.add(carattere.upper())
    print(insieme1)
    print(insieme2)
    lettere = "ABCDEFGHIJLMNOPQRSTUVWXYZ"
    alfabeto = set()
    for ch in lettere:
        alfabeto.add(ch)

    comuni = insieme1.intersection(insieme2)
    lettere1 = insieme1.difference(insieme2)
    lettere2 = insieme2.difference(insieme1)
    tutte = insieme1.union(insieme2)
    nessuna = alfabeto.difference(tutte)

    print("I caratteri che compaiono in entrambe le stringhe sono: ", comuni)
    print("I caratteri che compaiono sono nella prima stringa sono: ", lettere1)
    print("I caratteri che compaiono solo nella seconda stringa sono: ", lettere2)
    print("Le lettere che non compaiono nè nella prima stringa nè nella seconda stringa sono: ", nessuna)


main()