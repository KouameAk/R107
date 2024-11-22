from random import *

def bonchiffre():
    n = randint(0,100)
    r = int(input("Entre un chiffre : "))
    c = 0
    while r!=n:
        if r < n:
            print("C'est plus grand")
            r = int(input("Réessaie ! "))
            c += 1
        elif r > n:
            print("C'est plus petit")
            r = int(input("Réessaie ! "))
            c += 1
    return "Trouvé ! Tu a  essayé ", c, " fois"

print(bonchiffre())