def VerificationDate():
    L = str(input("Date : "))
    while len(L) != 8 or not L.isdigit():
        L = str(input("Entrez une date au bon format : "))

    d = int(L[:2])
    m = int(L[2:4])
    y = int(L[4:])

    bis = (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)

    dinm = [31, 29 if bis else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if m < 1 or m > 12:
        print(f"Le mois {m} n'existe pas.")
        return

    elif d < 1 or d > dinm[m - 1]:
        print(f"Le jour {d} n'existe pas pour le mois {m} en {y}.")
        return

    else:
        print(f"La date {L} est juste.")



print(VerificationDate())