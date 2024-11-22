def velo():
    debut = int(input("Donnez l'heure de début de la location (un entier) : "))
    fin = int(input("Donnez l'heure de fin de la location (un entier) : "))

    if not (0 <= debut <= 24 and 0 <= fin <= 24):
        print("Les heures doivent être comprises entre 0 et 24 !\n")
    elif debut == fin:
        print("Attention ! l'heure de fin est identique à l'heure de début.\n")
    elif debut > fin:
        print("Attention ! le début de la location est après la fin ...\n")
    else:
        t1 = 0
        t2 = 0
        r = 0.0

        for h in range(debut, fin):
            if 0 <= h < 7 or 17 <= h < 24:
                t1 += 1
                r += 1.0
            elif 7 <= h < 17:
                t2 += 1
                r += 2.0

        print("Vous avez loué votre vélo pendant")
        if t1 > 0:
            print(f"{t1} heure(s) au tarif horaire de 1.0 euro(s)")
        if t2 > 0:
            print(f"{t2} heure(s) au tarif horaire de 2.0 euro(s)")
        print(f"Le montant total à payer est de {r} euro(s).")
    return""

print(velo())
