from math import sqrt
base = float(input("Inserire la lunghezza della base del rettangolo: "))
altezza = float(input("Inserire la lunghezza dell'altezza del rettangolo: "))
area = base*altezza
perimetro = 2*base+2*altezza
diagonale = sqrt(base**2+altezza**2)
print("L'area del rettangolo vale: ", area)
print("Il perimetro del rettangolo vale: ", perimetro)
print("La lunghezza della diagonale del rettangolo vale: ", diagonale)
