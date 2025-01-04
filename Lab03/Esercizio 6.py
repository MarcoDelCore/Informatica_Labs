# Considerando i valori numerici dei voti spiegati nell’esercizio 2, scrivete un
# programma che traduca un numero compreso tra 0 e 4 nel voto letterale più vicino.
# Ad esempio, il numero 2.8 (che potrebbe essere la media di più voti) deve essere
# tradotto come B–. Risolvete i casi di parità in favore del voto migliore: ad esempio,
# 2.85 deve essere tradotto come B.
voto = float(input("Inserisci un voto numerico: "))
if voto >= 4.15:
    print("Il voto in lettere corrispondente è: A+")
elif voto >= 3.85:
    print("Il voto in lettere corrispondente è: A")
elif voto >= 3.55:
    print("Il voto in lettere corrispondente è: A-")
elif voto >= 3.15:
    print("Il voto in lettere corrispondente è: B+")
elif voto >= 2.85:
    print("Il voto in lettere corrispondente è: B")
elif voto >= 2.55:
    print("Il voto in lettere corrispondente è: B-")
elif voto >= 2.15:
    print("Il voto in lettere corrispondente è: C+")
elif voto >= 1.85:
    print("Il voto in lettere corrispondente è: C")
elif voto >= 1.55:
    print("Il voto in lettere corrispondente è: C-")
elif voto >= 1.15:
    print("Il voto in lettere corrispondente è: D+")
elif voto >= 0.85:
    print("Il voto in lettere corrispondente è: D")
elif voto >= 0.55:
    print("Il voto in lettere corrispondente è: D-")
elif voto >= 0:
    print("Il voto in lettere corrispondente è: F")
else:
    print("Il voto inserito non è classificabile")
