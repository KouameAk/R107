L = [0] * 3
print(L, id(L))
for i in range(len(L)):
    print(L[i], type(L[i]), id(L[i]))
L[1] += 1
for i in range(len(L)):
    print(L[i], type(L[i]), id(L[i]))

chaine = "machaine"
print(chaine, type(chaine), id(chaine))