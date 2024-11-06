def nbrmin():
    j = int(input("Inserer une valeur pour le jour : "))
    h = int(input("Inserer une valeur pour l'heure : "))
    m = int(input("Inserer une valeur pour les minutes : "))

    nbr = 0

    nbr = ((j-1) * 24 * 60) + (h * 60) + m

    return nbr

print(nbrmin())
