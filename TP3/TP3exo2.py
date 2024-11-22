import time
def decomptef():
    n = int(input("Entrez un nbr entier positif : "))
    print("Compte à rebours en for :")

    for i in range(n,-1,-1):
        print(i)
        time.sleep(1)

    return

print(decomptef())

def decomptew():
    n = int(input("Entrez un nbr entier positif : "))
    print("Compte à rebours en while :")

    while n >= 0:
        print(n)
        time.sleep(1)
        n -= 1
        
    return

print(decomptew())