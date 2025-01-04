# In una simulazione predatore-preda, si calcolano le popolazioni di predatori
# (predators) e prede (preys) usando le equazioni seguenti:
# preyn+1 = preyn × (1 + A – B × predn)
# predn+1 = predn × (1 – C + D × preyn)
# In queste equazioni, A è il ritmo con cui le nascite di prede sovrastano le loro morti
# naturali, B è il ritmo di predazione, C è il ritmo con cui le morti di predatori
# sovrastano le nascite in caso di assenza di cibo e D è il ritmo con cui aumentano i
# predatori in presenza di cibo.
# Scrivete un programma che chieda questi valori all’utente, oltre alle dimensioni
# iniziali delle popolazioni e al numero di intervalli di tempo che coinvolgono la
# simulazione. Successivamente, il programma deve visualizzare la dimensione delle
# due popolazioni per il numero di intervalli di tempo assegnato
prey_in = float(input("Inserire popolazione iniziale prede: "))
pred_in = float(input("Inserire popolazione iniziale predatori: "))
tempo = int(input("Inserire numero intervalli di tempo: "))
A = float(input("Ritmo con cui nascite di prede sovrastano morti naturali: "))
B = float(input("Ritmo di predazione: "))
C = float(input("Ritmo con cui morti di predatori sovrastano nascite in assenza di cibo: "))
D = float(input("Ritmo con cui aumentano predatori in presenza di cibo: "))

for i in range(1, tempo + 1):
    prey_fin = prey_in * (1 + A - B * pred_in)
    pred_fin = pred_in * (1 - C + D * prey_in)
    print("Dopo", i, "intervalli di tempo, la popolazione di prede diventa: %.1f" % prey_fin)
    print("Dopo", i, "intervalli di tempo, la popolazione di predatori diventa: %.1f " % pred_fin)
    prey_in = prey_fin
    pred_in = pred_fin
