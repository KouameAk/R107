def travail():
    heures_travail = int(input("Entrez le nombre d'heures travaillées : "))
    salaire_horaire = float(input("Entrez le salaire horaire : "))

    salaire_total = 0

    if heures_travail <= 160:
        salaire_total = heures_travail * salaire_horaire
    elif heures_travail <= 200:
        salaire_total = (160 * salaire_horaire) + ((heures_travail - 160) * salaire_horaire * 1.25)
    else:
        salaire_total = (160 * salaire_horaire) + (40 * salaire_horaire * 1.25) + ((heures_travail - 200) * salaire_horaire * 1.5)

    print(f"Le salaire total pour {heures_travail} heures travaillées est de {salaire_total:.2f} euros.")

print(travail())