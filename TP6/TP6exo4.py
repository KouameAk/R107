import random

def generer(nbr, vmin, vmax):
    L = []
    for i in range(nbr):
        L.append(random.randint(vmin, vmax))
    return L

def combienInferieur(table, vseuil):
    x = 0
    for i in table:
        if i < vseuil:
            x += 1
    return x


tab = generer(int(input("Combien de nombre vous voulez génére ?  ")), int(input("Quel est la valeur minimum : ")), int(input("Quel est la valeur maximum : ")))
tab.sort()
total = combienInferieur(tab, int(input("Quelle est la valeur seuil :  ")))
print(tab)
print(f"Il y en a {total} inférieurs à 25")