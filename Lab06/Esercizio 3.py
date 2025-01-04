# Scrivete una funzione, find(string, match), che verifichi se la stringa match è
# contenuta nella stringa string

def main():
    stringa = input("Inserisci una stringa: ")
    match = input("Inserisci una stringa match: ")
    corr = find(stringa, match)
    if corr == True:
        print("La stringa inserita è contenuta nella stringa principale.")
    else:
        print("La stringa inserita non è contenuta nella stringa principale.")

def find(string, match):
    if match in string:
        return True
    else:
        return False

main()
