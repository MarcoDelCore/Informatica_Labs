def main():
    operazioni = open('manutenzione.txt', 'r')
    parametri = open('parametri.txt', 'r')

    line = parametri.readline()
    riga = line.rstrip().split(',')
    data_rif = riga[0]
    data = riga[0].split('/')
    gg = int(data[0])
    mm = int(data[1])
    aaaa = int(data[2])
    rif = riga[1]

    diz_operazioni = {}
    for line in operazioni:
        riga = line.rstrip().split(',')
        diz_operazioni[riga[0]] = [riga[1], riga[2]]

    max_prezzo = 0
    op = []
    if rif == 'a':
        print(f'Le operazioni eseguite prima del {data_rif} sono:')
        for (key, val) in diz_operazioni.items():
            data2 = val[0].split('/')
            gg1 = int(data2[0])
            mm1 = int(data2[1])
            aaaa1 = int(data2[2])
            if aaaa >= aaaa1 and ((mm > mm1) or (mm == mm1 and gg > gg1)):
                operazione = key
                giorno = val[0]
                prezzo = int(val[1])
                print(operazione, 'in data', giorno, 'costo', prezzo, 'euro.')
                if prezzo > max_prezzo:
                    max_prezzo = prezzo
                op.append(operazione)
    elif rif == 'p':
        print(f'Le operazioni da eseguire dopo il {data_rif} sono:')
        for (key, val) in diz_operazioni.items():
            data2 = val[0].split('/')
            gg1 = int(data2[0])
            mm1 = int(data2[1])
            aaaa1 = int(data2[2])
            if aaaa <= aaaa1 and((mm<mm1) or (mm==mm1 and gg<gg1)):
                operazione = key
                giorno = val[0]
                prezzo = int(val[1])
                print(operazione, 'in data', giorno, 'costo', prezzo, 'euro.')
                if prezzo > max_prezzo:
                    max_prezzo = prezzo
                op.append(operazione)

    print()
    for (key, val) in diz_operazioni.items():
        if int(val[1]) == max_prezzo and key in op:
            if rif == 'a':
                print(f'La manutenzione più costosa è stata {key} del {val[0]} costata {val[1]} euro.')
            elif rif == 'p':
                print(f'La manutenzione più costosa da effettuare è {key} del {val[0]} costata {val[1]} euro.')

main()