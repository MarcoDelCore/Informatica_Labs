""""
 Scrivete la funzione:
 def countWords(string)
 che restituisca il numero di parole presenti nella stringa string.
"""


def main():
    str = input("Inserisci una stringa: ")
    parole = contaParole(str)
    print("La stringa inserita contiene %d parole" % parole)


def contaParole(stringa):
    parole = 1
    for i in stringa:
        if i.isspace():
            parole = parole + 1
    return parole


main()
