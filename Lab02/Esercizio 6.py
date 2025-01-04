num = input("Inserire un numero di telefono a 10 cifre: ")
if len(num) != 10:
    num = input("Inserire un numero di telefono a 10 cifre: ")
print("("+num[0]+num[1]+num[2]+")"+num[3]+num[4]+num[5]+"-"+num[6]+num[7]+num[8]+num[9])
print("("+num[0:3]+")"+num[3:6]+"-"+num[6:10])
print("("+num[:3]+")"+num[3:6]+"-"+num[6:])
