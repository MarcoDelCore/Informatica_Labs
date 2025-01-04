# Scrivete un’applicazione che gestisca la prevendita di un numero limitato di biglietti
# del cinema. Ogni acquirente può comprare al massimo 4 biglietti e non ne possono
# essere venduti più di 100. Il programma deve chiedere all’utente quanti biglietti
# intende acquistare, per poi visualizzare il numero di biglietti rimasti. L’operazione va
# ripetuta fino all’esaurimento dei biglietti, visualizzando al termine il numero di
# acquirenti.
biglietti = 100
n_acquirenti = 0
while biglietti > 0:
    print("Rimangono %d biglietti!" % biglietti)
    disp = min(4, biglietti)
    num = int(input("Quanti biglietti intende comprare? (max %d): " % disp))
    while num < 1 or num > min(4, biglietti):
        print("Numero non valido.")
        num = int(input("Quanti biglietti intende comprare? (max %d): " % disp))
    biglietti = biglietti - num
    n_acquirenti = n_acquirenti + 1
print("Numero acquirenti: %d" % n_acquirenti)
