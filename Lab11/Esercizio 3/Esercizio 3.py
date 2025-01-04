def main():
    array1 = {5:4, 9:2, 10:9}
    array2 = {3:9, 8:6, 10:6}
    somma = sparseArraySum(array1, array2)
    print("L'array somma è: ", somma)


def buildarray(diz):
    lista = []
    for key in diz:
        lista = [0] * (key + 1)
    for (key, val) in diz.items():
        lista[key] = val
    return lista


def sparseArraySum(diz1, diz2):
    array_1 = buildarray(diz1)
    array_2 = buildarray(diz2)

    if len(array_1) < len(array_2):
        somma = [0] * len(array_2)
        for i in range(len(array_2)):
            somma[i] = array_1[i] + array_2[i]

    else:
        somma = [0] * len(array_1)
        for i in range(len(array_1)):
            somma [i] = array_1[i] + array_2[i]

    return somma


main()
