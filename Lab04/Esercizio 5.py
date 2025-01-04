# Numeri primi. Scrivete un programma che chieda all’utente un numero intero e, poi,
# visualizzi tutti i numeri primi minori o uguali a tale numero
num = int(input("Inserisci un numero: "))
print("I numeri primi che precedono il numero", num, "sono i seguenti:")
primo = False
nonprimo = False
for i in range(1, num+1):
    primo = False
    nonprimo = False
    for j in range(2, i+1):
        if i != j and i % j != 0:
            primo = True
        elif i == j:
            primo = True
        else:
            nonprimo = True
    if primo and nonprimo == False:
        print(i)
