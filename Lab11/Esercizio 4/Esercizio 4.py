def main():
    numero = int(input("Inserisci un numero: "))
    numeri = set()
    for num in range(2, numero + 1):
        numeri.add(num)
    print(numeri)
    primi = numeri.copy()
    div = 2
    while div < numero:
        for num in primi:
            if num % div == 0 and num != div:
                numeri.discard(num)
        div += 1

    print(numeri)

main()
