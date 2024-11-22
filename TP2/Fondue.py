def fondue():
    base=4
    fromage=800.0
    eau=2
    ail=2
    pain=400
    nbConvives=int(input("Entrez le nombre de personne(s) conviées à la fondue : "))
    nouvFromage = 800.0 * nbConvives / base
    nouvEau = 2 * nbConvives / base
    nouvAil = 2 * nbConvives / base
    nouvPain = 400 * nbConvives / base

    print(f"Pour faire une fondue fribourgeoise pour {nbConvives} personnes, il vous faut : "
          f"\n- {nouvFromage} gr de fromage "
          f"\n- {nouvEau} dl d'eau "
          f"\n- {nouvAil} gousse(s) d'ail"
          f"\n- {nouvPain} gr de pain")

    return

print(fondue())