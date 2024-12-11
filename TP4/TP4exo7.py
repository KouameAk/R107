binome = ("login1", "login2")
print(f"L’étudiant {binome[0]} est en binôme avec l’étudiant {binome[1]}.")



nouvLogin = input("Entrez le nouveau login pour remplacer le second membre du binôme : ")
try:
    binome[1] = nouvLogin
except TypeError as e:
    print("Erreur :", e)



try:
    del binome[1]
except TypeError as e:
    print("Erreur :", e)



troisieme_login = input("Entrez le login pour former un trinôme : ")
trinome = binome + (troisieme_login,)
print(f"Le trinôme est composé des étudiants : {trinome[0]}, {trinome[1]} et {trinome[2]}.")
