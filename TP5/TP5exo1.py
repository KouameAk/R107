def nom():
    nom1=input("Entrez le nom de la première personne : ").strip()
    prenom1=input("Entrez le prenom de la première personne : ").strip()
    nom2=input("Entrez le nom de la deuxieme personne : ").strip()
    prenom2=input("Entrez le prenom de la deuxieme personne : ").strip()
    personne1 = f"{prenom1.capitalize()} {nom1.upper()}"
    personne2 = f"{prenom2.capitalize()} {nom2.upper()}"
    lignes = [personne1, personne2]
    lignes.sort()
    for ligne in lignes:
        print(ligne)

print(nom())