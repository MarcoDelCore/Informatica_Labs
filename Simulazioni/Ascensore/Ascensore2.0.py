def main():
    movimenti = open("movimenti.txt", "r")
    movimenti_risparmio = 0
    mivimenti_norisparmio = 0
    attuale_risparmio = 0
    attuale = 0

    for line in movimenti:
        piani = line.rstrip().split()
        partenza = int(piani[0])
        arrivo = int(piani[1])
        mov = abs(partenza - attuale)
        mivimenti_norisparmio += mov + abs(partenza - arrivo)
        attuale = arrivo
        if partenza < arrivo:
            mov_risparmio = abs(partenza - attuale_risparmio)
            movimenti_risparmio += (arrivo - partenza)
            movimenti_risparmio += mov_risparmio
            attuale_risparmio = arrivo

    consumo_risparmio = movimenti_risparmio * 100
    print("Ascensore con risparmio:")
    print(f"Spostamenti: {movimenti_risparmio} Consumo: {consumo_risparmio} W")

    consumo_norisparmio = mivimenti_norisparmio * 100
    print("Ascensore senza risparmio:")
    print(f"Spostamenti: {mivimenti_norisparmio} Consumo: {consumo_norisparmio} W")

    risparmio_assoluto = abs(consumo_risparmio - consumo_norisparmio)
    print(f"Risparmio assoluto: {risparmio_assoluto} W")

    risparmio_percentuale = (risparmio_assoluto * 100) / consumo_norisparmio
    risparmio_percentuale = round(risparmio_percentuale, 2)
    print(f"Risparmio percentuale: {risparmio_percentuale} %")

    movimenti.close()


main()
