def main():
    testo = open("input.txt", "r")
    out = open("output.txt", "w")
    riga = testo.readline()
    temp = ''
    while riga != '':
        temp = riga + temp
        riga = testo.readline()
    out.write(temp)
    testo.close()
    out.close()


main()
