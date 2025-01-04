# Scrivete un programma che traduca un voto in lettere nel corrispondente voto
# numerico. I voti in lettere sono A, B, C, D e F, eventualmente seguiti da un segno + o
# –. I loro valori numerici sono, nell’ordine, 4, 3, 2, 1 e 0. I voti F+ e F– non esistono.
# Un segno + aumenta il voto numerico di 0.3, mentre un segno – lo diminuisce della
# stessa quantità. Il voto A+ è comunque uguale a 4.0.
# Enter a letter grade: B–
# The numeric value is 2.7.
voto = input("Inserisci un voto in lettere: ")
if "A" in voto:
    if voto == "A+" or voto == "A":
        print("Il valore numerico è 4.0")
    else:
        print("Il valore numerico è 3.7")
elif "B" in voto:
    if voto == "B+":
        print("Il valore numerico è 3.3")
    elif voto == "B":
        print("Il valore numerico è 3.0")
    else:
        print("Il valore numerico è 2.7")
elif "C" in voto:
    if voto == "C+":
        print("Il valore numerico è 2.3")
    elif voto == "C":
        print("Il valore numerico è 2.0")
    else:
        print("Il valore numerico è 1.7")
elif "D" in voto:
    if voto == "D+":
        print("Il valore numerico è 1.3")
    elif voto == "D":
        print("Il valore numerico è 1.0")
    else:
        print("Il valore numerico è 0.7")
elif "F" in voto:
    if voto == "F+" or voto == "F-":
        print('Il voto inserito non esiste')
    else:
        print("Il valore numerico è 0")
else:
    print("Il voto inserito non esiste")

