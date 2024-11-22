def moyenne():
    n = int(input("Donnez le nombre d'etudiants : "))
    m = 0.0
    L = []
    s = 0
    for i in range(n):
        x = float(input(f"Note etudiant {i}: "))
        if 0 >= x <= 20:
            x = float(input("Donnez une moyenne compris entre 0 et 20 : "))
        L.append(x)
        s += x

    m = s / n
    print(f"Moyenne de classe : {m} ")
    print("Numéro de l’Etudiant | note | ecart a la moyenne")
    for i in range(n):
        y = L[i] - m
        print(f"{i} | {L[i]} | {y}")
    return""

print(moyenne())