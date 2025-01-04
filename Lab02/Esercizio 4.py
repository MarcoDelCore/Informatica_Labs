numero = int(input("Inserire il numero di libri: "))
costo = int(input("Inserire il costo totale dei  libri: "))
tasse = costo*0.075
spedizione = 2*numero
totale = costo + tasse + spedizione
print("Il totale dell'ordine è di %.2f dollari" % totale)
