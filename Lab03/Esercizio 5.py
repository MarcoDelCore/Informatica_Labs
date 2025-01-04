# Un anno di 366 giorni viene detto bisestile (leap) e serve a mantenere il calendario
# sincronizzato con il Sole, dal momento che la Terra vi ruota attorno una volta ogni
# 365.25 giorni. In realtà, questo numero non è esatto e per tutte le date successive al
# 1582 si applica la correzione gregoriana: solitamente gli anni divisibili per 4, come il
# 1996, sono bisestili, ma gli anni divisibili per 100, come il 1900, non lo sono; come
# eccezione all’eccezione, gli anni divisibili per 400, come il 2000, sono bisestili.
# Scrivete un programma che chieda all’utente un anno e determini se si tratta di un
# anno bisestile, usando un unico enunciato if (con gli opportuni operatori booleani).
anno = int(input("Inserire un anno: "))
if anno <= 1582 and anno % 4 == 0:
    print("L'anno inserito è bisestile")
elif anno > 1582 and anno % 100 == 0 and not anno % 400 == 0:
    print("L'anno inserito non è bisestile")
elif anno > 1582 and  anno % 4 == 0 or anno % 400 == 0:
    print("L'anno inserito è bisestile")
else:
    print("L'anno inserito non è bisestile")
