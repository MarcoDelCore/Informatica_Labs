# Un supermercato premia i propri clienti con buoni spesa il cui importo dipende dalla
# quantità di denaro spesa in prodotti alimentari (groceries). Ad esempio, spendendo
# 50 dollari, si ottiene un buono spesa di importo pari all’otto percento di quella
# somma. La tabella seguente mostra la percentuale usata per calcolare il buono spesa
# relativo a somme diverse. Scrivete un programma che calcoli e visualizzi il valore
# del buono spesa consegnato al cliente, sulla base della somma di denaro che ha speso
# nell’acquisto di prodotti alimentari
spesa = float(input("Inserire il denaro speso in prodotti alimentari: "))
if spesa < 10:
    buono = 0
elif spesa <= 60:
    buono = spesa*0.08
elif spesa <= 150:
    buono = spesa*0.1
elif spesa <= 210:
    buono = spesa*0.12
else:
    buono = spesa*0.14
print("Il buono spesa è di %.2f dollari" % buono)
