def analyse_chaine(chaine):

    if len(chaine) > 100:
        chaine = chaine[:100]

    voyelles = "aeiouyAEIOUY"
    taille = 0
    compteur_voyelles = 0
    sous_chaine = "wagon"
    taille_sous_chaine = len(sous_chaine)
    premiere_occurrence = -1
    nombre_occurrences = 0


    for i in range(len(chaine)):
        taille += 1
        if chaine[i] in voyelles:
            compteur_voyelles += 1


        if i <= len(chaine) - taille_sous_chaine and chaine[i:i + taille_sous_chaine] == sous_chaine:
            if premiere_occurrence == -1:
                premiere_occurrence = i
            nombre_occurrences += 1


    pourcentage_voyelles = (compteur_voyelles / taille) * 100 if taille > 0 else 0

    print(f"Taille de la chaîne : {taille} caractères")
    print(f"Pourcentage de voyelles : {pourcentage_voyelles:.2f}%")
    if premiere_occurrence != -1:
        print(f"La sous-chaîne 'wagon' commence à l'index {premiere_occurrence}.")
    else:
        print("La sous-chaîne 'wagon' n'existe pas.")
    print(f"Nombre d'occurrences de 'wagon' : {nombre_occurrences}")


chaine = input("Entrez une chaîne de caractères (maximum 100 caractères) : ")
analyse_chaine(chaine)