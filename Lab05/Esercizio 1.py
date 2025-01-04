# Scrivete un programma che legga tre stringhe e le visualizzi in ordine lessicografico.
stringa1 = input("Inserisci una stringa: ")
stringa2 = input("Inserisci una stringa: ")
stringa3 = input("Inserisci una stringa: ")
if stringa1 < stringa2 and stringa1 < stringa3:
    prima = stringa1
    if stringa2 < stringa3:
        seconda = stringa2
        terza = stringa3
    else:
        seconda = stringa3
        terza = stringa2
elif stringa2 < stringa1 and stringa2 < stringa3:
    prima = stringa2
    if stringa1 < stringa3:
        seconda = stringa1
        terza = stringa3
    else:
        seconda = stringa3
        terza = stringa1
else:
    prima = stringa3
    if stringa1 < stringa2:
        seconda = stringa1
        terza = stringa2
    else:
        seconda = stringa2
        ternza = stringa1
