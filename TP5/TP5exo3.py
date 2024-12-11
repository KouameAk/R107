def palindrome(chaine):
    chaine = chaine.lower()
    chaine_epuree = ''.join(c for c in chaine if c.isalpha())
    return chaine_epuree == chaine_epuree[::-1]

    chaine = input("Entrez un mot ou une phrase : ")

    if est_palindrome(chaine):
        print("C'est un palindrome !")
    else:
        print("Ce n'est pas un palindrome.")

print(palindrome(""))
