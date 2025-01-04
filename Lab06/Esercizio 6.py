# Scrivete un programma che converta un numero romano, come MCMLXXVIII, nella
# sua rappresentazione decimale.
def main():
    numero = input("Inserisci un numero romano: ")
    numero = numero.upper()
    totale = 0
    print(numero[0])
    print(numero[1])
    while len(numero) > 1:
        if ValoreDecimale(numero[0]) >= ValoreDecimale(numero[1]):
            totale += ValoreDecimale(numero[0])
            numero = numero.replace(numero[0], "", 1)
        else:
            totale += ValoreDecimale(numero[1]) - ValoreDecimale(numero[0])
            numero = numero.replace(numero[0], "", 1)
            numero = numero.replace(numero[0], "", 1)
    if len(numero) == 1:
        totale += ValoreDecimale(numero)
    print(f"Il corrispondente numero decimale è : {totale}")


def ValoreDecimale(lettera):
    if lettera == "I": valore = 1
    elif lettera == "V": valore = 5
    elif lettera == "X": valore = 10
    elif lettera == "L": valore = 50
    elif lettera == "C": valore = 100
    elif lettera == "D": valore = 500
    elif lettera == "M": valore = 1000
    else:
        exit("Valore non valido.")
    return valore


main()
