def pair():
    nbr = int(input("Entrez un nombre entier: "))
    if nbr == 0:
        print("Le nombre est zéro (et il est pair)")
    elif nbr > 0:
        if nbr % 2 == 0:
            print("Le nombre est positif et pair")
        else:
            print("Le nombre est positif et impair")
    else:
        if nbr % 2 == 0:
            print("Le nombre est négatif et pair")
        else:
            print("Le nombre est négatif et impair")

    return


print(pair())