def fact():
    f = int(input("Entrez un nombre :  "))
    r = 1
    for i in range(1, f + 1):
        r *= i
    return r

print(fact())