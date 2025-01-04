# Scrivete un programma per la conversione di unità di misura che chieda all’utente da
# quale unità (scegliendo tra: ml, l, g, kg, mm, cm, m, km) e verso quale unità
# (scegliendo tra: fl. oz, gal, oz, lb, in, ft, mi) vuole effettuare una conversione,
# rifiutando conversioni incompatibili (come, ad esempio, gal → km). Chiedete, poi, il
# valore da convertire e, infine, visualizzate il risultato:
# Convert from? gal
# Convert to? ml
# Value? 2.5
# 2.5 gal = 9463.5 ml
valore = float(input("Inserire il valore da convertire: "))
print("UNITA' DI MISURA DI PARTENZA:\n1=ml\n2=l\n3=g\n4=kg\n5=mm\n6=cm\n7=m\n8=km")
sel1 = int(input("Seleziona un'unità di misura di partenza: "))
print("UNITA' DI MISURA DI ARRIVO:\n1=fl.oz\n2=gal\n3=oz\n4=lb\n5=in\n6=ft\n7=mi")
sel2 = int(input("Inserire l'unità di misura di arrivo: "))

if sel1 == 1:
    val1 = "ml"
    if sel2 == 1:
        conversione = valore / 28.4
    elif sel2 == 2:
        conversione = valore / 4546.09
    else:
        conversione = "Error"
if sel1 == 2:
    val1 = "l"
    if sel2 == 1:
        conversione = valore / 0.02957
    elif sel2 == 2:
        conversione = valore / 4.54609
    else:
        conversione = "Error"
if sel1 == 3:
    val1 = "g"
    if sel2 == 3:
        conversione = valore / 28.349
    elif sel2 == 4:
        conversione = valore / 453.592
    else:
        conversione = "Error"
if sel1 == 4:
    val1 = "kg"
    if sel2 == 3:
        conversione = valore / 0.02835
    elif sel2 == 4:
        conversione = valore / 0.45359
    else:
        conversione = "Error"
if sel1 == 5:
    val1 = "mm"
    if sel2 == 5:
        conversione = valore / 25.4
    elif sel2 == 6:
        conversione = valore / 304.8
    elif sel2 == 7:
        conversione = valore / (1.609 * 10 ** 6)
    else:
        conversione = "Error"
if sel1 == 6:
    val1 = "cm"
    if sel2 == 5:
        conversione = valore / 2.54
    elif sel2 == 6:
        conversione = valore / 30.48
    elif sel2 == 7:
        conversione = valore / 160934
    else:
        conversione = "Error"
if sel1 == 7:
    val1 = "m"
    if sel2 == 5:
        conversione = valore / 0.0254
    elif sel2 == 6:
        conversione = valore / 0.3048
    elif sel2 == 7:
        conversione = valore / 1609.34
    else:
        conversione = "Error"
if sel1 == 8:
    val1 = "km"
    if sel2 == 5:
        conversione = valore / (2.54 * 10 ** -5)
    elif sel2 == 6:
        conversione = valore / 0.0003048
    elif sel2 == 7:
        conversione = valore / 1.60934
    else:
        conversione = "Error"
if sel2 == 1:
    val2 = "fl. oz"
elif sel2 == 2:
    val2 = "gal"
elif sel2 == 3:
    val2 = "oz"
elif sel2 == 4:
    val2 = "lb"
elif sel2 == 5:
    val2 = "in"
elif sel2 == 6:
    val2 = "ft"
elif sel2 == 7:
    val2 = "mi"
if conversione == "Error":
    print("Le unità di misura non sono compatibili")
else:
    print("Convert from: %s\nConvert to: %s\nValue: %.2f\n%.2f %s = %.2f %s" % (val1, val2, valore, valore, val1, conversione, val2))
