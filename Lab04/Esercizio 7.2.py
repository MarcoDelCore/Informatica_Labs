# Il gioco di Nim. Si tratta di un gioco molto noto, con un certo numero di varianti:
# quella qui descritta ha una strategia vincente davvero interessante. Due giocatori
# prelevano alternativamente biglie da un mucchietto. Ad ogni mossa, un giocatore
# sceglie quante biglie prendere: almeno una e al massimo metà delle biglie
# disponibili. Poi è il turno dell’altro giocatore. Il giocatore che prende l’ultima biglia
# perde la partita.
# Scrivete un programma che consenta all’utente di giocare contro il computer.
# Generate un numero intero compreso tra 10 e 100 e usatelo come dimensione iniziale
# del mucchietto di biglie. Generate un numero intero, 0 o 1, e utilizzatelo per decidere
# se sarà l’utente o il computer a giocare per primo. Generate un numero intero, 0 o 1,
# e usatelo per decidere se il computer giocherà in modo intelligente o stupido:
# giocando in modo stupido, ad ogni sua mossa il computer semplicemente preleva dal
# mucchietto un numero di biglie casuale (ma valido, cioè compreso tra 1 e n/2, se nel
# mucchietto sono rimaste n biglie); in modalità intelligente, invece, preleva un
# numero di biglie tale che il numero di quelle che rimangono nel mucchio sia una
# potenza di due diminuita di un’unità, cioè 3, 7, 15, 31 o 63. Quest’ultima è sempre
# una mossa valida, tranne quando la dimensione del mucchio è proprio uguale a una
# potenza di due diminuita di un’unità: in tal caso il computer fa una mossa scelta a
# caso (ovviamente tra quelle valide). Come potrete verificare sperimentalmente, il
# computer non può essere battuto quando gioca in modalità intelligente e fa la prima
# mossa, a meno che la dimensione iniziale del mucchio non sia 15, 31 o 63.
# Analogamente, un giocatore umano che faccia la prima mossa e conosca la strategia
# qui descritta è in grado di battere il calcolatore
from random import randint
# from math import log
UTENTE = 1
COMPUTER = 0
INTELLIGENTE = 1
STUPIDO = 0

n_biglie = randint(10, 100)
turno = randint(0, 1)
difficolta = randint(0, 1)

if difficolta == INTELLIGENTE:
    print("Il computer giocherà in modalità intelligente.")
else:
    print("Il computer giocherà in modalità stupida.")

if turno == UTENTE:
    print("Il primo turno lo giochi tu!")
else:
    print("Il primo turno lo gioca il computer!")

print("Si giocherà con %d biglie!" % n_biglie)

while n_biglie > 0:
    if turno == COMPUTER:
        if n_biglie == 1:
            biglie_prese = 1
        elif n_biglie == 3 or n_biglie == 7 or n_biglie == 15 or n_biglie == 31 or n_biglie == 63:
            biglie_prese = randint(1, (n_biglie//2))
        elif difficolta == INTELLIGENTE:
            # biglie_prese = n_biglie - 2**int(log(n_biglie, 2))+1
            if n_biglie > 63:
                biglie_prese = n_biglie - 63
            elif 31 < n_biglie < 63:
                biglie_prese = n_biglie - 31
            elif 15 < n_biglie < 31:
                biglie_prese = n_biglie - 15
            elif 7 < n_biglie < 15:
                biglie_prese = n_biglie - 7
            elif 3 < n_biglie < 7:
                biglie_prese = n_biglie - 3
        else:
            biglie_prese = randint(1, (n_biglie // 2))

        n_biglie = n_biglie - biglie_prese
        print("Il computer ha preso %d biglie. Ne rimangono %d." % (biglie_prese, n_biglie))
        turno = UTENTE

    elif turno == UTENTE:
        print("E' il tuo turno. ci sono %d biglie disponibili." % n_biglie)
        biglie_prese = int(input("Quante biglie vuoi prendere? "))
        while biglie_prese < 1 or biglie_prese > max(n_biglie//2, 1):
            print("Il numero inserito non è valido.")
            biglie_prese = int(input("Quante biglie vuoi prendere? "))
        n_biglie = n_biglie - biglie_prese
        print("Hai preso %d biglie. Ne rimangono %d." % (biglie_prese, n_biglie))
        turno = COMPUTER

if turno == COMPUTER:
    print("Il computer ha vinto!")
else:
    print("Hai vinto!")
