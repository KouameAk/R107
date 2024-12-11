def notes():
    notes = []
    coefficients = []

    for i in range(1, 6):
        saisie = input(f"Veuillez entrer la note du module {i} et le coefficient correspondant : ")
        note, coef = saisie.split()
        notes.append(float(note))
        coefficients.append(int(coef))

    somme_notes_coef = sum(note * coef for note, coef in zip(notes, coefficients))
    somme_coefficients = sum(coefficients)
    moyenne = somme_notes_coef / somme_coefficients

    admis = moyenne > 10 and all(note >= 8 for note in notes)

    print(f"\nMoyenne générale : {moyenne:.2f}")
    if admis:
        print("L'étudiant est admis.")
    else:
        print("L'étudiant n'est pas admis.")

print(notes())