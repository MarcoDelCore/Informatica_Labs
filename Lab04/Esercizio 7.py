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
n_biglie = randint(10, 100)
print("Il gioco si svolgerà con %d biglie" % n_biglie)

giocatore = randint(0, 1)
if giocatore == 0:
    print("Il primo a giocare è l'utente.")
else:
    print("Il primo a giocare è il computer")

difficolta = randint(0, 1)
# difficolta = int(input("Inserire livello difficoltà (0/1): "))
if difficolta == 0:
    print("Il computer giocherà in modalità intelligente")
else:
    print("Il computer giocherà in modalità stupida")


if giocatore == 0 and difficolta == 1:
    while n_biglie >= 1:
        if n_biglie > 1:
            biglie_prese = int(input("Selezionare la quantità di biglie da prendere: "))
            scelta = True
            while scelta == True:
                if biglie_prese > n_biglie/2 or biglie_prese < 1:
                    scelta = True
                    print("Il numero inserito non è valido, riprova con un altro numero.")
                    biglie_prese = int(input("Selezionare la quantità di biglie da prendere: "))
                else:
                    scelta = False
                    n_biglie = n_biglie - biglie_prese
                    print("Rimangono", n_biglie, "biglie")
        else:
            print("Il computer ha vinto")
            exit()
        if n_biglie > 1:
            rim = int(n_biglie/2)
            biglie_prese = randint(1, rim)
            print("Il compurer prende %d biglie" % biglie_prese)
            n_biglie = n_biglie - biglie_prese
            print("Rimangono", n_biglie, "biglie")
        else:
            print("L'utente ha vinto")
            exit()

elif giocatore == 1 and difficolta == 1:
    while n_biglie >= 1:
        if n_biglie > 1:
            rim = int(n_biglie/2)
            biglie_prese = randint(1, rim)
            print("Il compurer prende %d biglie" % biglie_prese)
            n_biglie = n_biglie - biglie_prese
            print("Rimangono", n_biglie, "biglie")
        else:
            print("L'utente ha vinto")
            exit()
        if n_biglie > 1:
            biglie_prese = int(input("Selezionare la quantità di biglie da prendere: "))
            scelta = True
            while scelta == True:
                if biglie_prese > n_biglie / 2 or biglie_prese < 1:
                    scelta = True
                    print("Il numero inserito non è valido, riprova con un altro numero.")
                    biglie_prese = int(input("Selezionare la quantità di biglie da prendere: "))
                else:
                    scelta = False
                    n_biglie = n_biglie - biglie_prese
                    print("Rimangono", n_biglie, "biglie")
        else:
            print("Il computer ha vinto")
            exit()

elif giocatore == 0 and difficolta == 0:
    while n_biglie >= 1:
        if n_biglie > 1:
            biglie_prese = int(input("Selezionare la quantità di biglie da prendere: "))
            scelta = True
            while scelta == True:
                if biglie_prese > n_biglie / 2 or biglie_prese < 1:
                    scelta = True
                    print("Il numero inserito non è valido, riprova con un altro numero.")
                    biglie_prese = int(input("Selezionare la quantità di biglie da prendere: "))
                else:
                    scelta = False
                    n_biglie = n_biglie - biglie_prese
                    print("Rimangono", n_biglie, "biglie")
        else:
            print("Il computer ha vinto")
            exit()
        if n_biglie > 1:
            if n_biglie > 63:
                biglie_prese = n_biglie - 63
                print("Il computer prende %d biglie" % biglie_prese)
                n_biglie = n_biglie - biglie_prese
                print("Rimangono %d biglie" % n_biglie)
            elif 31 < n_biglie < 63:
                biglie_prese = n_biglie - 31
                print("Il computer prende %d biglie" % biglie_prese)
                n_biglie = n_biglie - biglie_prese
                print("Rimangono %d biglie" % n_biglie)
            elif 15 < n_biglie < 31:
                biglie_prese = n_biglie - 15
                print("Il computer prende %d biglie" % biglie_prese)
                n_biglie = n_biglie - biglie_prese
                print("Rimangono %d biglie" % n_biglie)
            elif 7 < n_biglie < 15:
                biglie_prese = n_biglie - 7
                print("Il computer prende %d biglie" % biglie_prese)
                n_biglie = n_biglie - biglie_prese
                print("Rimangono %d biglie" % n_biglie)
            elif 3 < n_biglie < 7:
                biglie_prese = n_biglie - 3
                print("Il computer prende %d biglie" % biglie_prese)
                n_biglie = n_biglie - biglie_prese
                print("Rimangono %d biglie" % n_biglie)
            else:
                rim = int(n_biglie / 2)
                biglie_prese = randint(1, rim)
                print("Il compurer prende %d biglie" % biglie_prese)
                n_biglie = n_biglie - biglie_prese
                print("Rimangono", n_biglie, "biglie")
        else:
            print("L'utente ha vinto")
            exit()

elif giocatore == 1 and difficolta == 0:
    while n_biglie >= 1:
        if n_biglie > 1:
            if n_biglie > 63:
                biglie_prese = n_biglie - 63
                print("Il computer prende %d biglie" % biglie_prese)
                n_biglie = n_biglie - biglie_prese
                print("Rimangono %d biglie" % n_biglie)
            elif 31 < n_biglie < 63:
                biglie_prese = n_biglie - 31
                print("Il computer prende %d biglie" % biglie_prese)
                n_biglie = n_biglie - biglie_prese
                print("Rimangono %d biglie" % n_biglie)
            elif 15 < n_biglie < 31:
                biglie_prese = n_biglie - 15
                print("Il computer prende %d biglie" % biglie_prese)
                n_biglie = n_biglie - biglie_prese
                print("Rimangono %d biglie" % n_biglie)
            elif 7 < n_biglie < 15:
                biglie_prese = n_biglie - 7
                print("Il computer prende %d biglie" % biglie_prese)
                n_biglie = n_biglie - biglie_prese
                print("Rimangono %d biglie" % n_biglie)
            elif 3 < n_biglie < 7:
                biglie_prese = n_biglie - 3
                print("Il computer prende %d biglie" % biglie_prese)
                n_biglie = n_biglie - biglie_prese
                print("Rimangono %d biglie" % n_biglie)
            else:
                rim = int(n_biglie / 2)
                biglie_prese = randint(1, rim)
                print("Il compurer prende %d biglie" % biglie_prese)
                n_biglie = n_biglie - biglie_prese
                print("Rimangono", n_biglie, "biglie")
        else:
            print("L'utente ha vinto")
            exit()
        if n_biglie > 1:
            biglie_prese = int(input("Selezionare la quantità di biglie da prendere: "))
            scelta = True
            while scelta == True:
                if biglie_prese > n_biglie / 2 or biglie_prese < 1:
                    scelta = True
                    print("Il numero inserito non è valido, riprova con un altro numero.")
                    biglie_prese = int(input("Selezionare la quantità di biglie da prendere: "))
                else:
                    scelta = False
                    n_biglie = n_biglie - biglie_prese
                    print("Rimangono", n_biglie, "biglie")
        else:
            print("Il computer ha vinto")
            exit()
