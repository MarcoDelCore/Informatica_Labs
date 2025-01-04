# Scrivete la funzione:
# def countVowels(string)
# che restituisca il numero di vocali presenti nella stringa string.

def main():
    str = input("Inserisci una stringa: ")
    voc = contaVocali(str)
    print("La stringa inserita contiene %d vocali" % voc)

def contaVocali(string):
    vocali = 0
    for i in string:
        if i.lower() in "aeiou":
            vocali = vocali + 1
    return vocali

main()
