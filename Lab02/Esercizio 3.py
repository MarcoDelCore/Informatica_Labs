x = input("Scrivi una parola qualsiasi di almeno 6 lettere: ")
if len(x) < 6:
    x = input("Scrivi una parola qualsiasi di almeno 6 lettere: ")
print(x[0] + x[1] + x[2] + "..." + x[len(x)-3] + x[len(x)-2] + x[len(x)-1])
