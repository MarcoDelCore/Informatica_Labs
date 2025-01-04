num = int(input("Inserire un valore di 5 cifre: "))
if num < 0:
    num = int(input("Inserire un valore positivo: "))
num = str(num)
if len(num) != 5:
    num = input("Inserire un numero di 5 cifre: ")
print("La prima cifra di", num, "è: ", num[0])
print("La seconda cifra di", num, "è: ", num[1])
print("La terza cifra di", num, "è: ", num[2])
print("La quarta cifra di", num, "è: ", num[3])
print("La quinta cifra di", num, "è: ", num[4])
