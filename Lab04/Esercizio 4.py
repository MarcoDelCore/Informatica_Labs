# Scrivete un programma che legga una parola e la visualizzi al contrario. Se, ad
# esempio, l’utente fornisce la stringa “Ciao”, il programma deve visualizzare oaiC.
stringa = input("Inserisci una stringa: ")
lun = len(stringa)
for i in range ((lun-1), -1, -1):
    print(stringa[i], end='')
