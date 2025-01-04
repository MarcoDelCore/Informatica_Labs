# Scrivete una funzione che calcoli il saldo di un conto bancario dopo che siano
# trascorsi un dato numeri di anni, a partire da un dato saldo iniziale e con un dato
# tasso di interesse annuo, accreditando gli interessi annualmente.

def main():
    saldo_in = float(input("Inserisci il saldo iniziale: "))
    interesse = float(input("Inserisci il tasso d'interesse annuo: "))
    anni = int(input("Inserisci il numero di anni per calcolare i profiitti: "))
    saldo_fin = saldoBanca(saldo_in, anni, interesse)
    print(f"Il saldo finale è di {saldo_fin} dollari.")


def saldoBanca(saldo, anni, interesse):
    for i in range(1, anni + 1):
        saldo = saldo + (saldo*(interesse/100))
        print(f"Il saldo dopo {i} anni è di {saldo} dollari.")
    return saldo


main()
