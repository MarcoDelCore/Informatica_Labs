# Scrivete un programma che legga tre numeri e visualizzi il messaggio “increasing” se
# sono in ordine crescente, “decreasing” se sono in ordine decrescente e “neither” se
# non sono né in ordine crescente né in ordine decrescente. In questo esercizio
# crescente significa strettamente crescente, cioè ciascun valore deve essere maggiore
# del precedente (analogo significato ha il termine decrescente): la sequenza 3 4 4,
# quindi, non va considerata crescente.
num1 = float(input("Inserisci il primo numero: "))
num2 = float(input("Inserisci il secondo numero: "))
num3 = float(input("Inserisci il terzo numero: "))
if num1 < num2 < num3:
    print("I numeri che hai inserito sono in ordine crescente")
elif num1 > num2 > num3:
    print("I numeri che hai inserito sono in ordine decrescente")
else:
    print("I numeri che hai inserito non sono nè in ordine crescente nè in ordine decrescente")
