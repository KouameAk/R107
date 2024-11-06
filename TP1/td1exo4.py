def date():
    nbrmin = int(input("Donner un nombre de minute : "))
    jour = 1
    heure = 0
    minute = 0

    return nbrmin // (24 * 60) + 1

print(date())

