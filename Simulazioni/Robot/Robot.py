def main():
    traiettorie = open("traiettorie.txt", "r")
    x1 = x2 = y1 = y2 = 0
    movimenti1 = ''
    movimenti2 = ''

    nomi = input("Inserisci nomi robot separati da ';': ")
    robot = nomi.split(';')

    riga = traiettorie.readline()
    while riga != '':
        if robot[0] in riga:
            robot1 = riga.rstrip().split()
            x1 = int(robot1[1])
            y1 = int(robot1[2])
            movimenti1 = robot1[3]
        elif robot[1] in riga:
            robot2 = riga.rstrip().split()
            x2 = int(robot2[1])
            y2 = int(robot2[2])
            movimenti2 = robot2[3]
        riga = traiettorie.readline()

    caselle1 = movimenti(x1, y1, movimenti1)
    caselle2 = movimenti(x2, y2, movimenti2)

    comuni = caselle1.intersection(caselle2)
    num_comuni = len(comuni)

    print(f"Ci sono {num_comuni} caselle visitate da entrambi i robot.")
    traiettorie.close()


def movimenti(x, y, mov):
    caselle = [(x, y)]
    for i in range(0, len(mov) - 1, 2):
        if mov[i + 1] == 'v':
            if mov[i] == '+':
                y += 1
            else:
                y -= 1
        else:
            if mov[i] == '+':
                x += 1
            else:
                x -= 1
        casella = (x, y)
        caselle.append(casella)
    c = set(caselle)
    return c


main()
