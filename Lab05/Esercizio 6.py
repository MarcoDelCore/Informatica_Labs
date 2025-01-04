# In francese i nomi delle nazioni sono femminili quando terminano con la lettera e,
# altrimenti sono maschili, con l’eccezione dei nomi seguenti, che sono maschili anche
# se terminano con la e:
# • le Belize
# • le Cambodge
# • le Mexique
# • le Mozambique
# • le Zaïre
# • le Zimbabwe
# Scrivete un programma che acquisisca il nome di una nazione in francese e vi
# aggiunga l’articolo: “le” per i nomi maschili e “la” per quelli femminili, come “le
# Canada” o “la Belgique”. Se, però, il nome della nazione inizia con una vocale,
# l’articolo diventa “l’” (ad esempio, l’Afghanistan). Infine, per i paesi qui elencati,
# che hanno un nome plurale, si usa l’articolo “les”:
# • les Etats-Unis
# • les Pays-Bas
nazione = input("Inserire il nome di una nazione in francese: ")

if nazione[len(nazione)-1] == "e":
    if nazione == "Belize" or nazione == "Cambodge" or nazione == "Mexique" \
            or nazione == "Mozambique" or nazione == "Zaire" or nazione == "Zimbabwe":
        print("Le " + nazione)
    elif nazione[0] in "AEIOU":
        print("L\'" + nazione)
    else:
        print("La " + nazione)
elif nazione[0] in "AEIOU":
    if nazione == "Etats-Unis":
        print("Les " + nazione)
    else:
        print("L\'" + nazione)
elif nazione == "Pays-Bas":
    print("Les " + nazione)
