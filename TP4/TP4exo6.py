def tri(L):
    for i in range (len(L)):
        for j in range (i, len(L)):
            if L[i] > L[j]:
                L[i], L[j] = L[j], L[i]
        print(L)

L = [5, 2, 4, 8, 1, 3]
print(tri(L))

print(sorted(L))

print(L.sort())