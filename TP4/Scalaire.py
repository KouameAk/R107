def scalaire():
    v1 = []
    v2 = []
    s = 0
    n = int(input("Quelle est la taille de vos vecteurs [entre 1 et 10] ? "))

    print("\nSaisie du premier vecteur :")
    for i in range(n):
        x = int(input(f"v1[{i}] = "))
        v1.append(x)

    print("\nSaisie du second vecteur :")
    for i in range(n):
        x = int(input(f"v2[{i}] = "))
        v2.append(x)
        
    for i in range(n):
        s += v1[i]*v2[i]
    print(f"Le produit scalaire de v1 par v2 vaut {s:.1f}")

    return""



print(scalaire())