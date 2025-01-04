# Scrivete un programma che legga una stringa e visualizzi i messaggi appropriati,
# dopo aver verificato se:
# a. contiene soltanto lettere
# b. contiene soltanto lettere maiuscole
# c. contiene soltanto lettere minuscole
# d. contiene soltanto cifre
# e. contiene soltanto lettere e cifre
# f. inizia con una lettera maiuscola
# g. termina con un punto
stringa = input("Inserisci una stringa qualsiasi: ")
if stringa.isalpha():
    print("La stringa", stringa, "contiene soltanto lettere")
if stringa.isupper():
    print("La stringa", stringa, "contiene soltanto lettere maiuscole")
if stringa.islower():
    print("La stringa", stringa, "contiene soltantto lettere minuscole")
if stringa.isdigit():
    print("La stringa", stringa, "contiene soltanto cifre")
if stringa.isalnum():
    print("La stringa", stringa, "contiene soltanto lettere e cifre")
if stringa[0].isupper():
    print("La stringa", stringa, "inizia con una lettera maiuscola")
if stringa.endswith("."):
    print("La stringa", stringa, "termina con un punto")
