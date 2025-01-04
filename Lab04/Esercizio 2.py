# Scrivete programmi che leggano una riga di dati in ingresso sotto forma di stringa e
# visualizzino quanto segue:
# a. le sole lettere maiuscole della stringa;
# b. a partire dalla seconda lettera della stringa, una lettera viene visualizzata e
# l’altra no, alternativamente;
# c. la stringa con tutte le vocali sostituita da un carattere di sottolineatura
# (underscore);
# d. il numero di cifre presenti nella stringa;
# e. le posizioni di tutte le vocali presenti nella stringa.
stringa = input("Inserisci una stringa qualsiasi: ")
maiuscola = 0
pari = 0
voc = 0
pos_voc = 0
contatore = 0
vocali = "aeiouAEIOU"
print("Le lettere maiuscole sono: ", end=" ")
for i in stringa:
    if i.isupper():
        print(i, end=" ")
        maiuscola = 1
print()
if maiuscola == 0:
    print("Non ci sono lettere maiuscole")

print("Le lettere in posizione pari sono : ", end='')
for i in stringa:
    contatore = contatore + 1
    if contatore % 2 == 0:
        pari = 1
        print(i, end=' ')
print()
if pari == 0:
    print("Non ci sono lettere in posizioni pari.")

for i in stringa:
    if i in vocali:
        print("_", end="")
    else:
        print(i, end="")
print()

print("La stringa contiene", contatore, "lettere")

print("Le vocali sono nelle seguenti posizioni: ", end="")
for i in stringa:
    voc = voc + 1
    if i in vocali:
        pos_voc = voc
        print(pos_voc, end=' ')
