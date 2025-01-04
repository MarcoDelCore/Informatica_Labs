def main():
    spostamenti = open("movimenti.txt", "r")

    movimenti = []
    for line in spostamenti:
        movimento = line.rstrip().split()
        mov = [int(movimento[0]), int(movimento[1])]
        movimenti.append(mov)

    contatore1 = 0
    attuale1 = 0
    contatore2 = 0
    attuale2 = 0
    for elemento in movimenti:
        if contatore1 >= 1:
            if attuale1 < elemento[0]:
                for i in range(attuale1 + 1, elemento[0]):
                    contatore1 += 1
            elif attuale1 > elemento[0]:
                for i in range(elemento[0] + 1, attuale1):
                    contatore1 += 1
        if elemento[0] < elemento[1]:
            if contatore2 >= 1:
                if attuale2 < elemento[0]:
                    for i in range(attuale2 + 1, elemento[0]):
                        contatore2 += 1
                elif attuale2 > elemento[0]:
                    for i in range(elemento[0] + 1, attuale2):
                        contatore2 += 1
            for i in range(elemento[0], elemento[1] + 1):
                contatore1 += 1
                contatore2 += 1
            attuale2 = elemento[1]
        elif elemento[1] < elemento[0]:
            for i in range(elemento[1], elemento[0] + 1):
                contatore1 += 1
        attuale1 = elemento[1]
    consumo1 = contatore1 * 100

    print("Ascensore senza risparmio:")
    print(f"Spostamenti : {contatore1} Consumo: {consumo1} W")

    consumo2 = contatore2 * 100

    print("Ascensore con risparmio:")
    print(f"Spostamenti: {contatore2} Consumo: {consumo2} W")

    risparmio_assoluto = abs(consumo1 - consumo2)
    print(f"Risparmio assoluto: {risparmio_assoluto} W")

    risparmio_percentuale = (risparmio_assoluto * 100) / consumo1
    risparmio_percentuale = round(risparmio_percentuale, 2)
    print(f"Risparmio percentuale: {risparmio_percentuale} %")

    spostamenti.close()


main()
