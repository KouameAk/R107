def ajouter(L, x):
    L.append(x)
    return L

L1 = [0, 1, 2]
L2 = ajouter(L1, len(L1))
print(L1, type(L1), id(L1), L2, type(L2), id(L2))