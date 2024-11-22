def mult():
    n = float(input("Vous cherchez la table de multiplication de quel nombre : "))
    L = []
    for i in range(0,10):
        L.append(n * i)
        print (f"{n} * {i} = {n*i:.1f}")
    return ""


print(mult())
