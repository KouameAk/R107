L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6]

""" ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
* Completez le programme a partir d'ici.
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** * /
"""

def plusFrequent(liste):
    f = {}
    for nbr in liste:
        if nbr in f:
            f[nbr] += 1
        else:
            f[nbr] = 1
    max = 0
    elFrequent = liste[0]
    for nbr, occ in f.items():
        if occ > max:
            max = occ
            elFrequent = nbr

    print(f"Le nombre le plus frequent dans la liste est le : {elFrequent} ({max} x)")

plusFrequent(L1)

""" ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
* Ne rien modifier apres cette ligne.
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** * /
"""
