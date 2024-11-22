###################
### Question a)
###################
def somme():
    n = int(input("Entrez un entier : "))
    s = 0
    for i in range(n+1):
        s += i
    return n, s

#print(somme())


###################
### Question b)
###################
def bonchiffre():
    n = 100
    r = 0
    while r != n:
        r = int(input("Entrez le bon entier : "))
    return "Trouvé !"

#print(bonchiffre())


###################
### Question c)
###################

def comp():
    inf = 0
    entre = 0
    sup = 0

    for i in range(10):
        val = int(input("Entrez une valeur entre 0 et 20 : "))
        while val < 0 or val > 20:
            val = int(input("Erreur. Entrez une valeur entre 0 et 20 : "))

        if val < 10:
            inf += 1
        elif 10 <= val < 15:
            entre += 1
        else:
            sup += 1
    print("Nombre de valeurs < 10 :", inf)
    print("Nombre de valeurs >= 10 et < 15 :", entre)
    print("Nombre de valeurs >= 15 :", sup)
    return


#print(comp())

###################
### Question d)
###################


def maxsomme():
    n = int(input("Entrez un nombre : "))
    s = 0
    i = 0
    while s <= n:
        i += 1
        s += i
    return i - 1


print(maxsomme())
