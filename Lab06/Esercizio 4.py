def main():
    reddito = int(input("Inserisci il reddito annuo: "))
    contatore = 1
    while reddito > 0:
        figli = int(input("Inserisci il numero dei figli: "))
        suss = sussidio(reddito, figli)
        print(f'Il sussidio della famiglia {contatore} è di {suss} dollari')
        contatore = contatore + 1
        reddito = int(input("Inserisci un altro reddito annuo o -1 per uscire: "))

def sussidio(reddito, figli):
    if 30000 <= reddito < 40000 and figli >= 3:
        suss = 1000 * figli
    elif 20000 <= reddito < 30000 and figli >=2:
        suss = 1500 * figli
    elif reddito < 20000:
        suss = 2000 * figli
    else:
        suss = 0
    return suss

main()