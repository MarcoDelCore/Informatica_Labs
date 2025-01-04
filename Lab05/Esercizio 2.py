# Nell’ipotesi che il PIN dell’utente sia “1234”, scrivete un programma che chieda
# all’utente di digitare il PIN, consentendo al massimo tre tentativi e agendo in questo
# modo:
# • se l’utente inserisce il numero corretto, visualizzate il messaggio “Your PIN
# is correct” e terminate il programma;
# • se l’utente inserisce un numero sbagliato, visualizzate il messaggio “Your PIN
# is incorrect” e, se avete chiesto il PIN meno di tre volte, chiedetelo di
# nuovo;
# • se l’utente inserisce un numero sbagliato per tre volte, visualizzate il messaggio
# “Your bank card is blocked” e terminate il programma.
contatore = 1
PIN = False
PIN_CORRETTO = "1234"
pin = input("Inserire il proprio PIN: ")
while contatore < 3 and not PIN:
    if pin == PIN_CORRETTO:
        PIN = True
    else:
        print("Il PIN inserito non è corretto. Riprova.")
    pin = input("Inserire il proprio PIN: ")
    contatore = contatore + 1
if pin == PIN_CORRETTO:
    print("Il PIN è corretto.")
else:
    print("La carta di credito è stata bloccata.")
