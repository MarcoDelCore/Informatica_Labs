# Scrivete un programma che calcoli le tasse secondo questo schema. [P3.25]
stato_civile = input("Inserire il proprio stato civile: ")
reddito = float(input("Inserire il proprio reddito imponibile: "))
somma = float(input("Inserire la proria somma di denaro: "))
if stato_civile == "non coniugato":
    if reddito <= 8000:
        if somma >= 0:
            tasse = somma*0.1
    elif reddito <= 32000:
        if somma >= 8000:
            tasse = 800 + (somma*0.15)
    else:
        if somma >= 32000:
            tasse = 4400 + (somma*0.25)
else:
    if reddito <= 16000:
        if somma >= 0:
            tasse = somma*0.1
    elif reddito <= 64000:
        if somma >= 16000:
            tasse = 1600 + (somma*0.015)
    else:
        if somma >= 64000:
            tasse = 8800 + (somma*0.25)
print("Le tasse corrispondono a", tasse, "dollari")
