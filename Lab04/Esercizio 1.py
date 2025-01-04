# Scrivete programmi che leggano una sequenza di numeri interi e visualizzino quanto
# segue:
# a. il valore minimo e il valore massimo tra quelli acquisiti
# b. il numero di valori pari e il numero di valori dispari tra quelli acquisiti;
# c. le somme parziali di tutti i numeri acquisiti, calcolate e visualizzate dopo ogni
# nuova acquisizione (se, ad esempio, i valori in ingresso sono 1 7 2 9, il
# programma visualizzerà 1 8 10 19);
# d. i valori adiacenti duplicati (se, ad esempio, i valori acquisiti sono 1 3 3 4 5 5 6
# 6 6 3, il programma visualizzerà 3 5 6).
num = float(input("Inserisci un valore: "))
pari = 0
dispari = 0
if num % 2 == 0:
    pari = 1
else:
    dispari = 1
somma = num
num_str = input("Inserisci un valore o FINE: ")
num_str = num_str.upper()
massimo = num
minimo = num
num1 = num
while num_str != "FINE":
    num2 = float(num_str)
    if num2 < minimo:
        minimo = num2
    if num2 > massimo:
        massimo = num2
    if num2 % 2 == 0:
        pari = pari+1
    if num2 % 2 != 0:
        dispari = dispari+1
    somma = somma + num2
    print("La somma parziale è", somma)
    precedente = num1
    if num2 == num1:
        print(num2, "è un duplicato")
    num1 = num2
    num_str = input("Inserisci un valore o FINE: ")
    num_str = num_str.upper()
print("Il massimo è", massimo)
print("Il minimo è", minimo)
print("La somma finale è", somma)
print("Ci sono %d numeri pari" % pari)
print("Ci sono %d numeri dispari" % dispari)
