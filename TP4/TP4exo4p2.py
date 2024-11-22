L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6]

def plusFrequent(liste):
    max = 0
    el = liste[0]
    for nbr in liste:
        occ = liste.count(nbr)
        if occ > max:
            max = occ
            el = nbr

    print(f"Le nombre le plus frequent dans la liste est le : {el} ({max} x)")

plusFrequent(L1)